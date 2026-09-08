[![HoodL2.com presents Awesome Robinhood Chain](assets/hoodl2-banner.svg)](https://hoodl2.com)

# Awesome Robinhood Chain

A curated list of Robinhood Chain projects, developer resources and Stock Token research, maintained by **[HoodL2.com](https://hoodl2.com)**, an Autonomous Finance property.

**[Browse HoodL2](https://hoodl2.com/ecosystem) · [Stock Tokens](https://hoodl2.com/stocks) · [Learn](https://hoodl2.com/learn) · [All 129 directory records](directory/README.md)**

Reviewed **8 September 2026**. Project names link to their HoodL2 profiles; adjacent links lead to project websites or documentation. HoodL2 is independent of Robinhood and is not an official Robinhood publication.

## Contents

- [Start here](#start-here)
- [Network reference](#network-reference)
- [Exchanges and liquidity](#exchanges-and-liquidity)
- [Lending and stablecoins](#lending-and-stablecoins)
- [Bridges and interoperability](#bridges-and-interoperability)
- [RPC and developer infrastructure](#rpc-and-developer-infrastructure)
- [Oracles and data](#oracles-and-data)
- [Wallets and institutional services](#wallets-and-institutional-services)
- [More projects from HoodL2](#more-projects-from-hoodl2)
- [Agents and automation](#agents-and-automation)
- [Stock Tokens and issuer comparisons](#stock-tokens-and-issuer-comparisons)
- [Build on Robinhood Chain](#build-on-robinhood-chain)
- [HoodL2 reading list](#hoodl2-reading-list)
- [Directory and data](#directory-and-data)
- [Contribute](#contribute)

## Start here

- [HoodL2 ecosystem directory](https://hoodl2.com/ecosystem): project profiles, source notes and related infrastructure.
- [What is Robinhood Chain?](https://hoodl2.com/learn/what-is-robinhood-chain): HoodL2’s introduction to the network and its architecture.
- [Official Robinhood Chain documentation](https://docs.robinhood.com/chain/): network setup, contracts and integration guides.
- [Mainnet explorer](https://robinhoodchain.blockscout.com): inspect transactions, addresses and contracts.
- [Network status](https://status.robinhoodchain.offchain.io): operator status page.
- [Governance](https://docs.robinhood.com/chain/governance/): upgrade authority, security council and operational controls.

## Network reference

| Setting | Mainnet | Testnet |
| --- | --- | --- |
| Chain ID | `4663` | `46630` |
| Gas currency | ETH | ETH |
| Public RPC | `https://rpc.mainnet.chain.robinhood.com` | `https://rpc.testnet.chain.robinhood.com` |
| Explorer | [Blockscout](https://robinhoodchain.blockscout.com) | [Testnet explorer](https://explorer.testnet.chain.robinhood.com) |

Source: [Robinhood’s connection guide](https://docs.robinhood.com/chain/connecting/), checked 8 September 2026. Public RPC endpoints are rate limited; the guide recommends a provider for production. This is a configuration reference, not an uptime measurement.

## Reading the project list

Core infrastructure entries follow Robinhood’s [ecosystem overview](https://docs.robinhood.com/chain/), [provider list](https://docs.robinhood.com/chain/connecting/) and [bridge documentation](https://docs.robinhood.com/chain/bridging/), supplemented by HoodL2 records. Several projects operate across many chains. Check the exact product, network, supported assets and jurisdiction before using one. Inclusion does not establish endorsement, contract safety or available liquidity.

## Exchanges and liquidity

- [Uniswap](https://hoodl2.com/entity/uniswap): Swaps, liquidity pools and programmable markets. [Website](https://uniswap.org) · [Docs](https://docs.uniswap.org).
- [Rialto](https://hoodl2.com/entity/rialto): Spot exchange using a proprietary AMM; listed in Robinhood’s ecosystem documentation. [Website](https://rialto.xyz) · [Docs](https://docs.rialto.xyz/).
- [Arcus](https://hoodl2.com/entity/arcus): Stock Token spot beta for eligible users. Perpetuals use a waitlist and cohort rollout. [Website](https://arcus.xyz) · [Docs](https://docs.arcus.xyz).
- [Lighter](https://hoodl2.com/entity/lighter): Dedicated Robinhood Chain instance with its own contracts, sequencing and liquidity. [Website](https://robinhoodchain.lighter.xyz) · [Docs](https://docs.robinhood.com/chain/lighter-domains/).

## Lending and stablecoins

- [Morpho](https://hoodl2.com/entity/morpho): Lending markets and allocation vaults. Check each market’s collateral, oracle and risk parameters. [Website](https://morpho.org) · [Docs](https://docs.morpho.org).
- [USDG (Global Dollar)](https://hoodl2.com/entity/usdg): USD-backed Global Dollar stablecoin. Read the issuer’s reserve and redemption disclosures. [Website](https://globaldollar.com).
- [Paxos](https://hoodl2.com/entity/paxos): Issuer and financial infrastructure company behind USDG. [Website](https://www.paxos.com).

## Bridges and interoperability

Available routes vary by asset and network. Start with the [official bridging guide](https://docs.robinhood.com/chain/bridging/) and verify the destination token.

- [Robinhood Chain Bridge](https://hoodl2.com/entity/robinhood-chain-bridge): Canonical Ethereum connection. Withdrawals require a challenge period and a claim on Ethereum. [Docs](https://docs.robinhood.com/chain/bridging/).
- [LayerZero](https://hoodl2.com/entity/layerzero): Cross-chain messaging and omnichain token standards. [Website](https://layerzero.network) · [Docs](https://docs.layerzero.network).
- [Relay Protocol](https://hoodl2.com/entity/relay-protocol): Intent-based bridging and execution on the destination chain. [Website](https://relay.link) · [Docs](https://docs.relay.link).
- [Across](https://hoodl2.com/entity/across): Intent-based asset transfers across supported networks. [Website](https://across.to) · [Docs](https://docs.across.to).
- [LI.FI](https://hoodl2.com/entity/lifi): Aggregates bridge and swap routes. [Website](https://li.fi) · [Docs](https://docs.li.fi).
- [0x](https://hoodl2.com/entity/0x): Trading APIs and routing infrastructure. [Website](https://0x.org) · [Docs](https://0x.org/docs).

## RPC and developer infrastructure

- [Alchemy](https://hoodl2.com/entity/alchemy): RPC, indexed data and account abstraction services. [Website](https://www.alchemy.com) · [Docs](https://docs.alchemy.com).
- [QuickNode](https://hoodl2.com/entity/quicknode): Node endpoints and developer APIs. [Website](https://www.quicknode.com) · [Docs](https://www.quicknode.com/docs/robinhood).
- [Blockdaemon](https://hoodl2.com/entity/blockdaemon): Node infrastructure and institutional digital-asset services. [Website](https://www.blockdaemon.com).
- [dRPC](https://hoodl2.com/entity/drpc): RPC endpoints and request monitoring. [Website](https://drpc.org).
- [Validation Cloud](https://hoodl2.com/entity/validation-cloud): Node access and blockchain infrastructure. [Website](https://www.validationcloud.io).
- [Arbitrum](https://hoodl2.com/entity/arbitrum): The underlying chain technology and development documentation. [Website](https://arbitrum.io) · [Docs](https://docs.arbitrum.io).
- [Ethereum](https://hoodl2.com/entity/ethereum): Settlement network and broader Ethereum developer resources. [Website](https://ethereum.org) · [Docs](https://ethereum.org/developers).

## Oracles and data

- [Chainlink](https://hoodl2.com/entity/chainlink): Price feeds and cross-chain infrastructure. Stock Token integrations must account for feed freshness and market hours. [Website](https://chain.link) · [Docs](https://docs.robinhood.com/chain/oracles-and-price-feeds/).
- [Blockscout](https://hoodl2.com/entity/blockscout): Explorer software for reading transactions, token transfers and verified contracts. [Website](https://robinhoodchain.blockscout.com) · [Docs](https://docs.blockscout.com).
- [Allium](https://hoodl2.com/entity/allium): Indexed blockchain data for analytics and applications. [Website](https://www.allium.so) · [Docs](https://docs.allium.so).
- [CoinGecko](https://hoodl2.com/entity/coingecko): Token prices, market data and venue coverage. [Website](https://www.coingecko.com).
- [Zerion](https://hoodl2.com/entity/zerion): Wallet data APIs and a multichain self-custody wallet. [Website](https://zerion.io) · [Docs](https://zerion.io/api).

## Wallets and institutional services

- [Robinhood Wallet](https://hoodl2.com/entity/robinhood-wallet): Robinhood’s self-custody wallet. [Website](https://robinhood.com/wallet).
- [BitGo](https://hoodl2.com/entity/bitgo): Institutional digital-asset custody. [Website](https://www.bitgo.com).
- [Fireblocks](https://hoodl2.com/entity/fireblocks): Custody, tokenization and digital-asset operations. [Website](https://www.fireblocks.com).
- [TRM Labs](https://hoodl2.com/entity/trm-labs): Blockchain intelligence and transaction monitoring. [Website](https://www.trmlabs.com).

## More projects from HoodL2

Selected projects from our wider directory. These descriptions summarize the linked records and project materials; deployment details and current availability need individual review.

- [Alandale](https://hoodl2.com/entity/alandale): Swaps and liquidity incentives using a ve(3,3) model. [Website](https://alandale.xyz).
- [Ekubo](https://hoodl2.com/entity/ekubo): Concentrated-liquidity AMM with a singleton contract architecture. [Website](https://ekubo.org/).
- [Fables](https://hoodl2.com/entity/fables): Uniswap v4 hooks and ve(3,3) exchange mechanics. [Website](https://www.fables.fi/).
- [Longbow](https://hoodl2.com/entity/longbow): Lending project focused on USDG and tokenized-asset collateral. [Website](https://www.longbow.cash).
- [T3tris Finance](https://hoodl2.com/entity/t3tris-finance): Asynchronous ERC-4626 vault infrastructure. [Website](https://t3tris.finance/).
- [TrustSwap](https://hoodl2.com/entity/trustswap): Robinhood Chain resources for token launches and liquidity locks. [Website](https://trustswap.com/robinhood).
- [OpenSea](https://hoodl2.com/entity/opensea): Token and NFT marketplace with a Robinhood Chain discovery page. [Website](https://opensea.io/discover/chain/robinhood).
- [Yorozu](https://hoodl2.com/entity/yorozu): Browser MMO with AI-generated game content. [Website](https://www.yorozu.gg/).
- [StockRip](https://hoodl2.com/entity/stockrip): Pack-opening game using tokenized stocks. [Website](https://stockrip.com/).
- [Sounder Liquidity](https://hoodl2.com/entity/sounder-liquidity): Liquidity-depth and venue-dispersion analytics.

## Agents and automation

Agent tools differ in wallet permissions and execution controls. The linked profiles include source notes and gaps; this list does not verify trading permissions or contract deployments.

- [Aeron](https://hoodl2.com/entity/aeron): Agent software and public repositories for real-world assets. [Website](https://github.com/aeronlabs).
- [Project:VEX](https://hoodl2.com/entity/project-vex): Desktop agent for crypto research and onchain execution. [Website](https://www.projectvex.ai).
- [bankrbot](https://hoodl2.com/entity/bankr): Conversational trading, swaps and token limit orders. [Website](https://bankr.bot).
- [Sherwood Protocol](https://hoodl2.com/entity/sherwood-protocol): Vault infrastructure for agent-operated DeFi strategies. [Website](https://sherwood.sh).
- [wire bot](https://hoodl2.com/entity/wirebot): Social and web trading interfaces for Robinhood Chain. [Website](https://wirebot.trade/docs).

## Stock Tokens and issuer comparisons

Robinhood Stock Tokens are **tokenized debt securities issued by Robinhood Assets (Jersey) Limited**. They provide economic exposure to underlying shares or ETFs without granting legal or beneficial rights in those underlying securities. Read the [official Stock Token overview](https://docs.robinhood.com/chain/stock-tokens/) and the [issuer’s prospectus and final terms](https://docs.robinhood.com/rhj).

- [HoodL2 Stock Token directory](https://hoodl2.com/stocks): individual token records and linked research.
- [Stock Tokens explained](https://hoodl2.com/learn/stock-tokens-explained): how the instruments work and where risks arise.
- [Robinhood Stock Token issuer](https://hoodl2.com/learn/robinhood-stock-token-issuer): entity structure, custody, rights and redemption.
- [Compare Stock Token issuers](https://hoodl2.com/learn/stock-token-issuers-compared): the overview table and differences between product structures.

These comparisons cover distinct issuers, distributors and tokenization models. A comparison page does not mean the provider’s products are issued by Robinhood or available on Robinhood Chain.

| Compare with Robinhood | HoodL2 research |
| --- | --- |
| Coinbase | [Coinbase compared with Robinhood Stock Tokens](https://hoodl2.com/learn/coinbase-vs-robinhood-stock-tokens) |
| xStocks | [xStocks compared with Robinhood Stock Tokens](https://hoodl2.com/learn/xstocks-vs-robinhood-stock-tokens) |
| Ondo | [Ondo compared with Robinhood Stock Tokens](https://hoodl2.com/learn/ondo-vs-robinhood-stock-tokens) |
| Binance | [Binance compared with Robinhood Stock Tokens](https://hoodl2.com/learn/binance-vs-robinhood-stock-tokens) |
| Dinari | [Dinari compared with Robinhood Stock Tokens](https://hoodl2.com/learn/dinari-vs-robinhood-stock-tokens) |
| Superstate | [Superstate compared with Robinhood Stock Tokens](https://hoodl2.com/learn/superstate-vs-robinhood-stock-tokens) |
| Securitize | [Securitize compared with Robinhood Stock Tokens](https://hoodl2.com/learn/securitize-vs-robinhood-stock-tokens) |
| Swarm | [Swarm compared with Robinhood Stock Tokens](https://hoodl2.com/learn/swarm-vs-robinhood-stock-tokens) |
| Remora | [Remora compared with Robinhood Stock Tokens](https://hoodl2.com/learn/remora-vs-robinhood-stock-tokens) |

## Build on Robinhood Chain

| Task | Official reference | HoodL2 context |
| --- | --- | --- |
| Connect a wallet or RPC client | [Network configuration](https://docs.robinhood.com/chain/connecting/) | [Build on Robinhood Chain](https://hoodl2.com/learn/build-on-robinhood-chain) |
| Deploy a contract | [Foundry and Hardhat guide](https://docs.robinhood.com/chain/deploy-smart-contracts/) | [Developer overview](https://hoodl2.com/learn/build-on-robinhood-chain) |
| Identify a Stock Token contract | [Token contracts](https://docs.robinhood.com/chain/contracts/) | [Verify a canonical Stock Token](https://hoodl2.com/learn/verify-a-canonical-stock-token) |
| Integrate Stock Tokens | [Building with Stock Tokens](https://docs.robinhood.com/chain/building-with-stock-tokens/) | [Integration guide](https://hoodl2.com/learn/building-with-stock-tokens) |
| Read prices | [Oracles and price feeds](https://docs.robinhood.com/chain/oracles-and-price-feeds/) | [Stock Token prices and oracles](https://hoodl2.com/learn/stock-token-prices-and-oracles) |
| Handle dividends and splits | [Stock Token mechanics](https://docs.robinhood.com/chain/stock-tokens/) | [Dividends and splits](https://hoodl2.com/learn/stock-token-dividends-and-splits) |
| Sponsor gas or use smart accounts | [Account abstraction](https://docs.robinhood.com/chain/account-abstraction/) | [Developer overview](https://hoodl2.com/learn/build-on-robinhood-chain) |
| Integrate Lighter’s Robinhood instance | [API documentation](https://apidocs.rh.lighter.xyz/docs/get-started) | [Lighter profile](https://hoodl2.com/entity/lighter) |
| Run a node | [Full-node guide](https://docs.robinhood.com/chain/run-a-full-node/) | [Network profile](https://hoodl2.com/entity/robinhood-chain) |

## HoodL2 reading list

- [Bridging to Robinhood Chain](https://hoodl2.com/learn/bridging-to-robinhood-chain)
- [USDG and the dollar stack](https://hoodl2.com/learn/usdg-and-the-dollar-stack)
- [The sequencer and first-come, first-served ordering](https://hoodl2.com/learn/the-sequencer-and-fcfs-ordering)
- [Robinhood Chain compared with other L2s](https://hoodl2.com/learn/robinhood-chain-vs-other-l2s)
- [Where to see Robinhood Chain data](https://hoodl2.com/learn/where-to-see-robinhood-chain-data)
- [All HoodL2 guides](https://hoodl2.com/learn)
- [HoodL2 on YouTube](https://www.youtube.com/@hoodl2com)

## Directory and data

The [full directory](directory/README.md) contains **129 public HoodL2 records**, grouped by category and searchable with your browser’s Find command. It includes community projects, adjacent infrastructure and entries whose source records still have gaps. It is broader than this curated reading list.

The same snapshot is available as [JSON](data/projects.json), with stable entity slugs, HoodL2 profile URLs and recorded project links. It excludes internal confidence scores and blanket availability labels. The snapshot date is 8 September 2026; [HoodL2.com](https://hoodl2.com/ecosystem) carries subsequent editorial updates.

See [Sources and review notes](SOURCES.md) for provenance, current-source corrections and limits. Maintainers can regenerate the directory from the checked-in JSON with:

```sh
python3 scripts/render_directory.py
python3 scripts/render_directory.py --check
```

## Contribute

Suggest a project, correct a link or add a primary source using [the contribution guide](CONTRIBUTING.md). Include the HoodL2 profile when one exists, the exact product or deployment, and a dated source. Changes are reviewed before inclusion.

---

Maintained by **[HoodL2.com](https://hoodl2.com)** · An **Autonomous Finance** property · Independent Robinhood Chain research.
