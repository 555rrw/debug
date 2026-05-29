---
name: marketplace-price-researcher
description: "Price research assistant for browsing and searching product websites to compare prices, shipping, and seller risks. Use for: market research, price comparison, identifying best deals, and analyzing seller reliability across various platforms."
---

# Marketplace Price Researcher

This skill transforms the agent into a specialized price research assistant. It provides a structured workflow for searching, extracting, and normalizing product data from multiple online marketplaces to assist users in making informed purchasing decisions.

## When to Use
- When a user wants to find the best price for a specific product across multiple platforms.
- When researching market trends for specific items (e.g., electronics, collectibles).
- When comparing new vs. used conditions for the same product model.
- When evaluating total costs including shipping fees and platform service charges.

## When NOT to Use
- **DO NOT** use for automated purchasing or checkout.
- **DO NOT** use for sending messages to sellers.
- **DO NOT** perform any unconfirmed operations using the user's account.
- **DO NOT** use for real-time high-frequency trading or scalping.

## Supported Sources
Includes but is not limited to:
- **Taiwan/Regional:** Shopee (蝦皮), Carousell (旋轉拍賣), Yahoo Auction (Yahoo 奇摩拍賣), Ruten (露天拍賣), momo, PChome, Books.com.tw (博客來).
- **Global:** Amazon, eBay, Facebook Marketplace.
- **General:** Any publicly accessible product pages or search results.

## Search Workflow
1. **Identify Product Details:** Extract exact model names, specifications (RAM, Storage, Color), and condition (New/Used) from user request.
2. **Platform Search:** Execute searches on multiple target platforms. Use specific keywords to filter results.
3. **Data Extraction:** For each relevant result, capture:
   - Listed Price
   - Shipping Fees
   - Condition (New, Used, Like New, etc.)
   - Seller Rating/Reviews
   - Location/Region
4. **Verification:** Cross-reference extracted data. If information is missing or ambiguous, mark as "unverified".
5. **Availability Check:** If a site is inaccessible or requires login, mark as "unavailable". **NEVER** hallucinate data.

## Product Matching Rules
- **Strict Matching:** Only include items that match the exact model and specifications.
- **Variant Handling:** Group different specifications (e.g., 128GB vs 256GB) separately if requested.
- **Condition Segregation:** Always distinguish between Brand New, Open Box, and Used items.

## Price Normalization Rules
- **Currency:** Convert all prices to a single base currency (usually the user's local currency) if multiple currencies are found.
- **Total Calculation:** Total Estimated Price = Listed Price + Shipping Fee + Platform Fees (if applicable).
- **Unit Price:** For bulk items, calculate price per unit.

## Shipping & Fee Handling
- Check if shipping is free or calculated based on location.
- Include platform-specific service fees or payment processing fees if visible.
- Note any "Cash on Delivery" (COD) options or surcharges.

## Seller Risk & Condition Checks
- **Seller Rating:** Note the number of transactions and positive feedback percentage.
- **Risk Warning:** Flag listings with suspiciously low prices, new accounts with no feedback, or "stock photos" only.
- **Scam Alert:** Explicitly warn the user if a listing appears to be a scam or a fake/counterfeit product.

## Final Comparison Table Format
Present the findings in a clear, tabular format:

| Platform | Product Name | Condition | Listed Price | Shipping | Total (Est.) | Seller Risk | Source URL |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Name] | [Model/Spec] | [New/Used] | [Amount] | [Amount] | [Amount] | [Low/Med/High] | [Link] |

- **Listed Price:** The price shown on the page.
- **Shipping:** Estimated shipping cost.
- **Total Estimated Price:** Final cost to the user.
- **Checked Date:** Current date of the research.
- **Status:** If unavailable, mark the row as "unavailable".

## Prohibitions
- **NO** automatic ordering or adding to cart.
- **NO** private messaging to sellers.
- **NO** account-level changes or settings modifications.
- **NO** hallucination of prices, stock levels, or URLs.
