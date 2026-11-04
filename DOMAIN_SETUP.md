# Publish zooglass.io

The intended canonical address is `https://zooglass.io/`. `www.zooglass.io`
should redirect to it. This guide describes setup; it is not evidence that the
repository, Pages or DNS has already been configured.

## 1. Repository and review

Create `sproates/zooglass-website` with an initial README. Use public visibility
for GitHub Free, or private if the account plan supports private-repository Pages.
Allow the GitHub integration access if it is restricted to selected repositories.

Add the website files on a feature branch and open a pull request. Review the
pages and validation result, then merge when ready to publish. The Actions
workflow validates PRs and deploys only `main`. Only the `site/` directory becomes
the website; repository documentation and scripts are not deployed.

## 2. Verify domain ownership

Open the personal account's [Pages settings](https://github.com/settings/pages),
add `zooglass.io`, and obtain the exact TXT challenge from GitHub.

In GoDaddy, open the domain's DNS management page. Add the TXT record using the
name and value GitHub provides. The expected name is
`_github-pages-challenge-sproates`; use GitHub's displayed instructions as the
source of truth. Return to GitHub to verify it. Keep the TXT record afterwards.
Never invent a verification token.

## 3. Configure Pages before routing DNS

In the website repository's Settings → Pages:

- Set Source to **GitHub Actions**.
- Set Custom domain to **zooglass.io**.
- After the approved website changes reach `main`, confirm the Website workflow
  deploys successfully.

With Actions deployments, the repository `CNAME` file alone does not configure
the custom domain. Save it in Pages settings too.

## 4. Configure GoDaddy DNS

Use these records for GitHub Pages. For GoDaddy, `@` means `zooglass.io`.

| Type | Name | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | sproates.github.io |

Use the registrar's default TTL. Inspect existing records first. Replace only
conflicting website/parking records for `@` and `www`; retain mail (MX), SPF,
DKIM, verification and unrelated records. Existing AAAA records for another
host must not remain pointed at that host. If enabling IPv6, use GitHub's four
current Pages AAAA records from the documentation linked below.

Do not enable domain forwarding, use a wildcard record, or put a repository
path in the CNAME value. The same `sproates.github.io` target can serve multiple
custom-domain sites: GitHub routes each by its configured hostname.

## 5. HTTPS and discovery

Wait for DNS validation and GitHub's certificate provisioning. Enable **Enforce
HTTPS** when GitHub makes it available. Check the apex and `www` addresses,
including the redirect and certificate, before describing the site as live.
DNS and certificate changes can take time; recheck actual status rather than
assuming completion.

In Google Search Console, add a domain property for `zooglass.io`, copy its own
TXT verification token into GoDaddy and verify. Submit
`https://zooglass.io/sitemap.xml`. Inspect and request indexing for the homepage,
`/how-it-works/` and `/about/`. Keep the token out of site source files.

Update the public ZooGlass repository's website field to `https://zooglass.io/`
and add a reciprocal link from its README in a separate reviewed change after
the site is live. The website already links back to the project and creator.

## References

- [GitHub: custom-domain setup and DNS values](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [GitHub: verify a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [Google Search Console](https://search.google.com/search-console/)
