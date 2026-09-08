# Sources and review notes

Publisher: [HoodL2.com](https://hoodl2.com), an Autonomous Finance property. Review date: **8 September 2026**.

## HoodL2 source data

The directory snapshot comes from the [public HoodL2 entity API](https://hoodl2.com/api/v1/entities?limit=200), which returned 129 records at retrieval. Every record links to its source profile. Curated descriptions also draw on the source notes in those profiles. The [Learn collection](https://hoodl2.com/learn) supplies the linked educational articles and issuer comparisons.

`data/projects.json` preserves names, entity slugs, categories, profile URLs and recorded public project links. It omits source confidence scores, numerical metrics and broad network-status labels. No private dossiers, account details or local databases are included.

The full directory is a source snapshot, not a separate verification of 129 deployments. Its recorded project links may be older than the current-source links selected for the main README. Missing websites remain missing rather than being inferred from a project’s name.

## Primary sources checked for the main list

| Source | Used for |
| --- | --- |
| [Robinhood Chain overview](https://docs.robinhood.com/chain/) | Chain architecture, ecosystem resources and direct project links |
| [Connecting to Robinhood Chain](https://docs.robinhood.com/chain/connecting/) | Chain IDs, gas currency, explorers, public RPC and provider list |
| [Bridging](https://docs.robinhood.com/chain/bridging/) | Canonical bridge, withdrawal process and listed cross-chain services |
| [Stock Tokens](https://docs.robinhood.com/chain/stock-tokens/) | Issuer identity, debt-security structure and underlying-share rights |
| [RHJ documents](https://docs.robinhood.com/rhj) | Destination for the prospectus and final terms |
| [Lighter Domains](https://docs.robinhood.com/chain/lighter-domains/) | Dedicated Robinhood instance, separation from Lighter Core, UI and API docs |
| [Arcus](https://arcus.xyz) | Spot beta availability, perps waitlist/cohort rollout and linked documentation |
| [Rialto documentation](https://docs.rialto.xyz/) | Spot exchange and AMM description |

The linked project websites and documentation supply their own product descriptions. The provider table in Robinhood’s documentation does not establish that every product from those companies is available on the chain.

## Current-source corrections

- **Lighter:** the main list links to `robinhoodchain.lighter.xyz`, the dedicated Robinhood Chain instance documented by Robinhood. The full snapshot retains HoodL2’s recorded general Lighter links. Lighter Core and the Robinhood instance have separate contracts, sequencing and liquidity.
- **Arcus:** Robinhood’s current overview supplies `arcus.xyz`; the site links to `docs.arcus.xyz`. Its page distinguishes open spot beta for eligible users from a perps waitlist and cohort rollout. The snapshot has no recorded website for Arcus, so the new website is only asserted in the curated list.
- **Rialto:** the current Robinhood overview supplies `rialto.xyz`, supplementing the documentation link in the HoodL2 snapshot.

## Scope and limits

The selection includes multichain providers and adjacent Ethereum infrastructure alongside Robinhood Chain projects. It does not imply exclusivity, endorsement, audited contracts or guaranteed liquidity. Community and agent-project entries have additional source and deployment gaps described in their HoodL2 profiles.

Issuer comparison links describe different financial and distribution models. They are reading resources, not a list of equivalent instruments or confirmed Robinhood Chain deployments. Availability can depend on jurisdiction and participant eligibility.

The link check covered 234 distinct destinations, including all 129 HoodL2 profiles, and 40 local file or section links. All HoodL2 destinations and local links passed. Four project homepages returned automated-access challenges: Arbitrum (403), Ekubo (403), Relay (429) and CoinGecko (403). Their canonical links are retained from the source records; those responses do not establish an outage. External website links appearing only in the full directory were preserved from the snapshot and were not all rechecked.

Links and documentation were checked during preparation. No wallet connection, transaction, deposit or trading test was performed. A reachable page confirms a destination exists; it does not establish the safety or operation of a service.

## Format reference

The user supplied [adrydevel/awesome-robinhood-chain](https://github.com/adrydevel/awesome-robinhood-chain) as a format reference. This repository’s text, category selection, HoodL2 links and directory snapshot were prepared independently from HoodL2 data and the sources above.

The banner uses HoodL2’s colors and Space Grotesk, distributed under the [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/spacegrotesk/OFL.txt). It contains original vector artwork and outlined text; no Robinhood logo is used.
