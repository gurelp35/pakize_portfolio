# Pakize Gurel — Developer Portfolio

A responsive, accessible portfolio presenting frontend, full-stack and UX work for graduate and junior software engineering opportunities.

**Live website:** https://gurelp35.github.io/pakize_portfolio/  
**GitHub:** https://github.com/gurelp35  
**LinkedIn:** https://www.linkedin.com/in/pakize-gurel-7998b52a3/

> **Deployment note:** The professional redesign is under review in [Pull Request #1](https://github.com/gurelp35/pakize_portfolio/pull/1). Until that PR is approved and merged, the live GitHub Pages site may show the previous design.

## Selected projects

| Project | Focus | Links |
| --- | --- | --- |
| CareerPilot AI | Next.js, React, TypeScript; application tracking, job description analysis and interview preparation | [Live demo](https://careerpilot-ai-platform-six.vercel.app/) · [Source](https://github.com/gurelp35/careerpilot_ai_platform) |
| Software Engineering Project | Collaborative Node.js, Express, MySQL and Docker web application | Screenshots in portfolio |
| CalmSpace | Wellbeing web experience with breathing exercises and mood tracking | Screenshots in portfolio |
| Healthy Bite | Responsive nutrition website | [Source](https://github.com/gurelp35/healthy-bite-web-desing) |
| Grevio | Sustainable rewards mobile UX prototype | Screenshots in portfolio |

## Technology

This portfolio is a static HTML and CSS site hosted on GitHub Pages. It uses no runtime JavaScript or build dependencies. Project imagery is stored in `assets/`.

## Run locally

1. Clone the repository.
2. Open `index.html` in a browser, or serve the folder locally:

```bash
python3 -m http.server 8000
```

3. Visit http://localhost:8000/.

## Quality checks

Run the built-in standard-library tests:

```bash
python3 -m unittest discover -s tests -v
```

The tests check internal anchor targets, duplicate IDs, image files and alt text, safe external links, basic metadata, a single H1, and responsive/reduced-motion CSS rules. GitHub Actions also runs these checks on pull requests and pushes to `main`.

**Limitations:** These are source-level integrity checks, not a substitute for browser-based responsive layout, keyboard, contrast, or screen-reader testing. Before publishing, review the site at mobile, tablet and desktop widths and verify the live demo links.

## Deployment

GitHub Pages publishes from the repository's configured deployment source. Changes in feature branches or draft pull requests do **not** update the live site. Merge only after review and approval.

## Contact

Email: [pakizegurel@hotmail.com](mailto:pakizegurel@hotmail.com)
