---
name: decompose-fixed-capacity-revenue-into-yield-and-load
kind: decision
category: analytic-method
one_liner: Manage a fixed-capacity business by splitting performance into price-per-used-unit (yield) and utilization (load), since revenue is their product times capacity — and break-even utilization falls with your relative cost position.
source_book: Competition Demystified
source_run: 2026-06-13-greenwald-v1
extraction_contract: v1
perspective_origin: [quant]
source_anchors: [ch12¶20, ch12¶41]
promoted: 2026-06-13
status: promoted
---

## When to use
Any business whose capacity is fixed in the short run and perishable (airline seats, hotel rooms, ad inventory, SaaS seats, fixed networks), where you must price dynamically and judge entry/survival.

## Method
1. **Split the two factors.** Yield = revenue ÷ used capacity (a price proxy). Load = used capacity ÷ available capacity (utilization). Revenue ≈ yield × load × capacity.
2. **Optimize the product, not one factor.** A fixed asset earns only on price × fill rate; dynamic pricing trades yield for load to maximize the product, rather than chasing occupancy or price alone.
3. **Break-even utilization from cost position.** A lower unit cost lowers the load needed to cover fixed costs. Quantify your cost gap vs the incumbent (% per unit of output) and translate it into the minimum utilization for survival — a concrete go/no-go threshold for entry.
4. Use the same yield/load lens to spot where a low-price entrant does the most damage to a high-fixed-cost incumbent.

## Inputs → Outputs
- Inputs: revenue, used capacity, available capacity, your unit-cost gap vs incumbents, fixed-cost level.
- Outputs: current yield and load, the revenue-maximizing price/fill trade-off, and the break-even utilization threshold.

## Failure modes / assumptions
- Chasing load with deep price cuts can destroy yield faster than it fills capacity — optimize the product.
- A low break-even load helps survival but doesn't create a moat; pair with the moat-detection skill before assuming durable profit.
- Requires data systems to measure and adjust price by remaining availability; subscale players often can't.

## Worked example (illustrative, single)
An airline tracks yield = revenue/RPM and load = RPM/ASM and uses dynamic pricing to maximize their product; a low-cost entrant running ~20% below the incumbent's cost per passenger-mile can break even at roughly a 50% load factor, defining whether entry is viable.
