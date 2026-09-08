# Contributing to Awesome Robinhood Chain

Thank you for helping maintain [HoodL2’s Robinhood Chain resource list](https://hoodl2.com). Submit a pull request or repository issue with a specific addition or correction.

## Add or update a resource

Include:

- Project name, official URL and HoodL2 profile URL, if one exists.
- A short description of what it does.
- The relevant product, chain and deployment. Distinguish a mainnet integration from a testnet, announcement or general EVM compatibility.
- A primary source and the date you checked it. Documentation, project repositories and issuer filings are useful; an X announcement needs a direct post URL.
- Any known limits: waitlist, region, unsupported route, missing contracts or unclear ownership.

Link to canonical websites. Avoid referral URLs, shortened links, unsupported rankings, yield promises and claims of Robinhood endorsement. A project appearing in this list does not establish an audit or a recommendation to transact.

## Choose the right file

Edit `README.md` for the curated list and resource guides. For the full directory, update `data/projects.json` and regenerate `directory/README.md`:

```sh
python3 scripts/render_directory.py
python3 scripts/render_directory.py --check
```

Keep existing entity slugs stable. Record material factual changes, sources and check dates in `SOURCES.md`. Check local links and the destinations you change. A successful HTTP response alone does not verify a product claim.

## Publication and attribution

HoodL2 maintains the editorial copy and branding. Third-party names and marks belong to their respective owners. Keep the HoodL2 credit and source links in proposed changes.

Repository visibility is controlled by the maintainers. Opening a pull request does not authorize making the repository public or publishing the material elsewhere.
