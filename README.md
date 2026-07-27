# Joan's Tech Stuff

Personal blog at [joanfihu.com](https://joanfihu.com), migrated from WordPress to Astro + GitHub Pages.

## Local development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
npm run preview
```

## Deploy

Pushes to `main` deploy via GitHub Actions to GitHub Pages.

### Custom domain DNS

In your domain registrar (where `joanfihu.com` is registered), point DNS at GitHub Pages:

**Apex (`joanfihu.com`)** — A records:

| Type | Host | Value |
|------|------|-------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

**Optional www** — CNAME:

| Type | Host | Value |
|------|------|-------|
| CNAME | `www` | `webeng.github.io` |

Then in the GitHub repo: **Settings → Pages → Custom domain** → `joanfihu.com` → enable **Enforce HTTPS**.

After DNS propagates and the site looks good on Pages, cancel the WordPress.com paid plan.

## Content

- Posts: `src/content/blog/*.md`
- Images: `public/uploads/`
- Re-import from a WordPress WXR export: `python3 scripts/import_wordpress.py` (edit the export path in the script first)
