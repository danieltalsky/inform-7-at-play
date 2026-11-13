# Regenerate the theme's favicon set using Windows System.Drawing.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$output = Join-Path $PSScriptRoot '../themes/at-play/assets/favicons'
New-Item -ItemType Directory -Path $output -Force | Out-Null

$svg = @'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <rect width="256" height="256" fill="#f8f7f2"/>
  <path d="M64 80 128 128 64 176" fill="none" stroke="#242c35" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="184" cy="166" r="14" fill="#963b35"/>
</svg>
'@
[System.IO.File]::WriteAllText((Join-Path $output 'favicon.svg'), $svg)

# Draw the same geometry at 4x resolution before reducing to each raster size.
$master = [System.Drawing.Bitmap]::new(1024, 1024)
$canvas = [System.Drawing.Graphics]::FromImage($master)
$pen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml('#242c35'), 24)
$dot = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml('#963b35'))
try {
    $canvas.Clear([System.Drawing.ColorTranslator]::FromHtml('#f8f7f2'))
    $canvas.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $canvas.ScaleTransform(4, 4)
    $pen.StartCap = $pen.EndCap = [System.Drawing.Drawing2D.LineCap]::Round
    $pen.LineJoin = [System.Drawing.Drawing2D.LineJoin]::Round
    $points = [System.Drawing.PointF[]]@(
        [System.Drawing.PointF]::new(64, 80),
        [System.Drawing.PointF]::new(128, 128),
        [System.Drawing.PointF]::new(64, 176))
    $canvas.DrawLines($pen, $points)
    $canvas.FillEllipse($dot, 170, 152, 28, 28)
    foreach ($size in @(16, 32, 48, 180, 256)) {
        $bitmap = [System.Drawing.Bitmap]::new($size, $size)
        $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
        try {
            $graphics.Clear([System.Drawing.ColorTranslator]::FromHtml('#f8f7f2'))
            $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
            $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
            $graphics.DrawImage($master, 0, 0, $size, $size)
            $name = if ($size -eq 180) { 'apple-touch-icon.png' } else { "favicon-$size.png" }
            $bitmap.Save((Join-Path $output $name), [System.Drawing.Imaging.ImageFormat]::Png)
        } finally {
            $graphics.Dispose()
            $bitmap.Dispose()
        }
    }
} finally {
    $dot.Dispose()
    $pen.Dispose()
    $canvas.Dispose()
    $master.Dispose()
}

# ICO directory entries point to embedded PNG images (including a 256px entry).
$sizes = @(16, 32, 48, 256)
$stream = [System.IO.File]::Create((Join-Path $output 'favicon.ico'))
$writer = [System.IO.BinaryWriter]::new($stream)
try {
    $writer.Write([uint16]0)
    $writer.Write([uint16]1)
    $writer.Write([uint16]$sizes.Count)
    $offset = 6 + 16 * $sizes.Count
    foreach ($size in $sizes) {
        $bytes = [System.IO.File]::ReadAllBytes((Join-Path $output "favicon-$size.png"))
        $dimension = if ($size -eq 256) { 0 } else { $size }
        $writer.Write([byte]$dimension)
        $writer.Write([byte]$dimension)
        $writer.Write([uint16]0)
        $writer.Write([uint16]1)
        $writer.Write([uint16]32)
        $writer.Write([uint32]$bytes.Length)
        $writer.Write([uint32]$offset)
        $offset += $bytes.Length
    }
    foreach ($size in $sizes) {
        $writer.Write([System.IO.File]::ReadAllBytes((Join-Path $output "favicon-$size.png")))
    }
} finally {
    $writer.Dispose()
}
