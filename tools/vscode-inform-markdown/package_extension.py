"""Package this declarative extension as a VSIX using the standard library."""

import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

SOURCE = Path(__file__).resolve().parent
ROOT = SOURCE.parent.parent
NAMESPACE = "http://schemas.microsoft.com/developer/vsx-schema/2011"


def main():
    package = json.loads((SOURCE / "package.json").read_text(encoding="utf-8"))
    ET.register_namespace("", NAMESPACE)

    def child(parent, name, attrs=None, text=None):
        element = ET.SubElement(parent, f"{{{NAMESPACE}}}{name}", attrs or {})
        element.text = text
        return element

    manifest = ET.Element(f"{{{NAMESPACE}}}PackageManifest", {"Version": "2.0.0"})
    metadata = child(manifest, "Metadata")
    child(metadata, "Identity", {"Language": "en-US", "Id": package["name"],
                                 "Version": package["version"], "Publisher": package["publisher"]})
    child(metadata, "DisplayName", text=package["displayName"])
    child(metadata, "Description", {"{http://www.w3.org/XML/1998/namespace}space": "preserve"},
          package["description"])
    child(metadata, "Categories", text=",".join(package["categories"]))
    properties = child(metadata, "Properties")
    for name, value in {
        "Microsoft.VisualStudio.Code.Engine": package["engines"]["vscode"],
        "Microsoft.VisualStudio.Code.ExtensionDependencies": ",".join(package["extensionDependencies"]),
        "Microsoft.VisualStudio.Code.ExtensionPack": "",
        "Microsoft.VisualStudio.Code.LocalizedLanguages": "",
        "Microsoft.VisualStudio.Code.EnabledApiProposals": "",
        "Microsoft.VisualStudio.Code.PreRelease": "false",
    }.items():
        child(properties, "Property", {"Id": name, "Value": value})
    installation = child(manifest, "Installation")
    child(installation, "InstallationTarget", {"Id": "Microsoft.VisualStudio.Code"})
    child(manifest, "Dependencies")
    assets = child(manifest, "Assets")
    files = {
        "Microsoft.VisualStudio.Code.Manifest": "package.json",
        "Microsoft.VisualStudio.Services.Content.Details": "README.md",
        "Microsoft.VisualStudio.Services.Content.License": "LICENSE",
    }
    for kind, name in files.items():
        child(assets, "Asset", {"Type": kind, "Path": "extension/" + name, "Addressable": "true"})
    output = ROOT / "prototype/build" / f'{package["name"]}-{package["version"]}.vsix'
    output.parent.mkdir(parents=True, exist_ok=True)
    content_types = ('<?xml version="1.0" encoding="utf-8"?>'
                     '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                     '<Default Extension="json" ContentType="application/json"/>'
                     '<Default Extension="md" ContentType="text/markdown"/>'
                     '<Default Extension="vsixmanifest" ContentType="text/xml"/>'
                     '<Override PartName="/extension/LICENSE" ContentType="text/plain"/>'
                     '</Types>')
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("extension.vsixmanifest", ET.tostring(manifest, encoding="utf-8", xml_declaration=True))
        for name in (*files.values(), "syntaxes/inform7-markdown.tmLanguage.json"):
            archive.write(SOURCE / name, "extension/" + name)
    print(output)


if __name__ == "__main__":
    main()
