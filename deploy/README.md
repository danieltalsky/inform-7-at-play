# FTPS deployment

The public site is **https://informatplay.danieltalsky.com/**.
The site is built into `dist/`. The existing **Executable documentation** workflow
tests the export, compiles and plays every Inform example, and saves the site as
the `static-site` artifact. A successful push or manual run on `maestra` then
deploys that exact artifact when deployment is enabled. Pull requests only run
checks. Deployment jobs run one at a time and skip superseded revisions.

## One-time setup

Create the subdomain and a dedicated, password-authenticated FTPS account whose
login directory is exactly its public document root. The account should be
restricted to that directory. No remote shell access is required. The deployment
mirrors the **contents** of `dist` into the login directory (`.`), including
deleting remote files and directories absent from the build. Any required
`.htaccess` or other public server files must therefore be included in the build.

In the repository's **Settings → Secrets and variables → Actions**, add:

| Repository secret | Value |
| --- | --- |
| `FTP_USERNAME` | Dedicated FTPS login name. |
| `FTP_PASSWORD` | That account's password. |

The connection uses explicit TLS on port 21 and verifies the server certificate.
Both login and file transfers require encryption. No SSH key or host-key secret
is needed. Use the provider's secure FTP hostname if the domain's `ftp` alias
does not match the certificate.

Add these repository **variables**:

| Variable | Value |
| --- | --- |
| `FTP_HOST` | Server hostname or IPv4 address, without `ftp://` or a path. It need not match the public subdomain. |
| `FTP_PORT` | Optional; defaults to `21`. |
| `DEPLOY_ENABLED` | Set to `true` after the account, secrets, and destination are ready. Missing or any other value disables deployment. |

Configure DNS and HTTPS for `informatplay.danieltalsky.com` at the hosting
provider. All site links are relative; the build needs no domain setting.

## First deployment and routine updates

After enabling deployment, open **Actions → Executable documentation → Run
workflow**, selecting `maestra`. Verify that both the checks and **Deploy via
FTPS** succeed, then open the HTTPS site and check a chapter and its styling.
Changes to secrets or variables alone do not trigger a deployment.

After the first deployment, make changes through feature branches and PRs to
`maestra`. Merging a PR triggers checks and then deployment automatically.
Set `DEPLOY_ENABLED` to `false` to pause future deployments.

The mirror uploads files and removes stale files in place; it is not an atomic
site swap. A failed transfer can leave a partially updated site. Fix the
connection and rerun the latest `maestra` workflow to converge on the build.
To roll back, revert the relevant change through a PR and deploy the resulting
new revision. Older workflow runs are skipped if their commit is no longer the
tip of `maestra`.

GitHub Pages' legacy Jekyll deployment is separate from this workflow. It remains
enabled until explicitly retired; it does not publish the themed `dist` output.

Implementation: [lftp mirror and FTPS documentation](https://lftp.yar.ru/lftp-man.html).
