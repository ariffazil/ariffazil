# Spatial Intelligence Doctrine v0.1
## arifOS Cross-Agent Governance Doctrine
**Applies to:** All agents serving arifOS (Hermes, Gemini, OpenCode, or any future agent)
**Sovereign:** Arif bin Fazil
**Classification:** Governance doctrine — not optional guidance
**Last updated:** 2026-08-04

---

## 1. Spatial Capability Registry

Every spatial source used by an agent MUST be classified into exactly one access mode before the agent makes a capability or factual claim.

| Mode | Meaning | Typical examples | Trust condition |
|---|---|---|---|
| **INTERNAL** | Deterministic computation performed locally from inputs already available to the agent. No network service or external data lookup is required. | Coordinate validation, H3 indexing when locally implemented, distance and bearing calculations, bounding-box mathematics, polygon operations, coordinate-reference-system transforms | Verifiable from inputs and method |
| **CONNECTOR** | Data or computation obtained through a live external API, service, tool, database, or governed organ. | Geocoding, routing, geological databases, spatial catalog search, map-feature queries, remote H3 services | Valid only after live verification in the current session |
| **BROWSER** | Visual observation of a rendered spatial surface. The agent observes pixels or rendered interface content rather than querying a structured spatial data source. | Map screenshots, rendered globes, visible route displays, imagery viewed in a browser | Descriptive only; no implied semantic or API access |
| **UNAVAILABLE** | The required source is not integrated, not reachable, not authorized, rate-limited beyond use, or otherwise cannot answer the query in the current session. | An unprovisioned mapping platform, a failed connector, an exhausted quota, an inaccessible private dataset | No factual claim may be attributed to the source |

A configured connector is not necessarily a live connector. A visible map is not necessarily a queryable map. Platform availability MUST be established from current-session evidence rather than assumed from documentation, training recall, or prior sessions.

When several modes could answer a question, use the least powerful sufficient mode. INTERNAL computation is preferred when it fully answers the query; use a CONNECTOR only when external data or computation is required. BROWSER evidence is limited to what is visibly present. Use UNAVAILABLE when no verified route exists.

---

## 2. Spatial Claim Taxonomy

Every factual sentence about a place, coordinate, route, boundary, geological unit, imagery asset, or spatial relationship MUST carry exactly one epistemic label.

| Label | Meaning | Required use |
|---|---|---|
| `OBS_SPATIAL` | Direct observation made in the current session | Use for content directly observed from a current tool result or rendered spatial view |
| `API_SPATIAL` | Structured data returned by an API, connector, database, or service | Cite the source, query context, and timestamp or cache age |
| `DER_SPATIAL` | Result computed from stated spatial inputs | State the inputs and method, such as haversine distance, coordinate transform, or polygon operation |
| `INT_SPATIAL` | Interpretation based on spatial evidence and domain knowledge | Use for reasoned geographic or geological interpretation; do not present it as direct observation |
| `SPEC_SPATIAL` | Unverified hypothesis or tentative possibility | Use when evidence is incomplete or the claim is proposed for testing |
| `UNKNOWN` | No verified source supports the requested spatial claim | Use for explicit uncertainty or refusal; do not fill the gap with plausible recall |

Rules:

1. Split compound sentences when they contain claims of different epistemic types.
2. Training-data recall is never `OBS_SPATIAL` or `API_SPATIAL`; it is `INT_SPATIAL`, `SPEC_SPATIAL`, or `UNKNOWN` depending on evidential support.
3. Precision MUST match evidence. A country, region, or ambiguous place name does not justify an exact coordinate.
4. Cached API data remains `API_SPATIAL`, but its cache age MUST be disclosed.

---

## 3. No “Entire Map” Rule

No agent may claim internal possession of an entire map, globe, imagery archive, spatial database, or vendor platform.

When asked whether it has all of Google Maps, Google Earth, Macrostrat, global satellite imagery, or any equivalent platform, the agent MUST answer in substance:

> No internal possession. I can only route a bounded query to a connector that exists, is authorized, and is verified live in this session. A platform known from training or visible in a browser is not the same as live structured access.

The agent MUST then do one of the following:

- verify an appropriate connector and run a bounded query;
- offer a verified alternative source;
- ask permission or request needed query details; or
- declare the capability `UNAVAILABLE`.

Never describe theoretical, documented, or prior-session capability as current capability. Never imply that access to one endpoint, tile, layer, screenshot, or record grants access to an entire platform.

---

## 4. Source-Routed Response Format

Every non-trivial spatial answer MUST follow this order:

1. **Resolve** — identify the place, coordinate, geometry, route endpoints, or area of interest, including ambiguity or uncertainty.
2. **Declare source** — state `INTERNAL`, `CONNECTOR`, `BROWSER`, or `UNAVAILABLE`; name the actual source and whether it was verified in this session.
3. **Coverage** — state what the selected source can answer for this query.
4. **Freshness** — state whether the evidence is live, cached, dated, visually observed, or based on non-live recall.
5. **Limits** — state what the source cannot establish.
6. **Answer** — provide the result, labeling each factual sentence with the Spatial Claim Taxonomy.

Use this template:

```markdown
### Spatial answer — <topic>

**Location resolved:** <place, coordinates or geometry, and uncertainty>
**Source used:** INTERNAL | CONNECTOR · <source> · verified <yes/no in this session> | BROWSER · <surface> | UNAVAILABLE
**Coverage:** <what the source can establish for this query>
**Freshness:** <live timestamp | cache age | dataset date | observed now | non-live recall>
**Limits:** <what the source cannot establish>
**Claim labels used:** <labels present in the answer>

<label> <answer sentence>
```

If no source can support the requested claim, the answer MUST use `UNKNOWN`, state the unavailable capability, and offer a concrete next step without inventing a result.

---

## 5. Connector Verification Protocol

Before every connector-dependent top-level spatial answer, verify the connector in the current session. Use the lightest safe operation that establishes reachability and payload validity.

### 5.1 Identify the route

Record the intended connector, the capability needed, the expected response type, and any required authorization or governed-session context. A connector registration, configuration entry, or tool description alone is not proof of reachability.

### 5.2 Probe reachability

Use a read-only health endpoint, capability listing, metadata query, or deterministic smoke query. The probe SHOULD be low cost, bounded, and free of mutation. Record the time and result.

### 5.3 Resolve authorization gates

A session-init, lane-enforcement, authentication, or authorization response proves that the service is reachable but does not yet prove that the requested data is available. Establish the required governed session or authorization through the platform’s approved mechanism, then re-probe. Do not classify a reachable-but-gated service as dead.

### 5.4 Validate the response

Confirm that the response has the expected structure, status, coordinate reference system where relevant, and non-error payload. Empty, malformed, HTML-instead-of-JSON, or shape-mismatched responses MUST be treated as failures until explained; they may indicate rate limiting, an upstream error, or a changed API.

### 5.5 Declare one status

| Verification result | Required declaration |
|---|---|
| Valid data returned | `CONNECTOR · verified live this session` |
| Service responds with a governed-session or authorization gate | `CONNECTOR · reachable, authorization/session required` |
| Connection refused, DNS failure, or timeout | `UNAVAILABLE · connector unreachable this session` |
| Authentication or permission denied | `UNAVAILABLE · authorization failed this session` |
| Quota exhausted | `UNAVAILABLE · quota exhausted` |
| Rate limit received | `UNAVAILABLE · rate-limited`, including retry timing when known |
| Malformed or unexpected payload | `UNAVAILABLE · connector response not validated` |

Only a successful, validated data response authorizes `API_SPATIAL` claims. A health response establishes service reachability, not the truth of a location-specific result; the actual bounded query must still be run and validated.

---

## 6. Known Spatial Sources Inventory

This inventory is a governance baseline, not proof of live availability. Each agent MUST verify its own route in the current session and may classify a source as `UNAVAILABLE` even when another agent can reach it.

| Source | Baseline access mode | Coverage | Limits |
|---|---|---|---|
| **H3 spatial index** | INTERNAL when locally implemented; otherwise CONNECTOR | Hex-cell indexing, coordinate-to-cell conversion, neighborhood rings, polygon fill, aggregation | No map tiles, visualization, place names, terrain, or semantic attributes |
| **GEOX spatial services** | CONNECTOR when provisioned | Governed spatial, geological, basin, catalog, and indexing capabilities exposed by the federation | Capability varies by deployed surface; requires current-session reachability, authorization, and query verification |
| **Macrostrat** | CONNECTOR when provisioned | Stratigraphic units, geologic maps and columns, lithology, age, and related deep-time context | Coverage varies geographically; requires a live query; absence of a record is not proof of geological absence |
| **STAC catalogs** | CONNECTOR when provisioned | Discovery and metadata for cloud-native imagery and geospatial assets, including catalog-dependent Sentinel, Landsat, Copernicus, or commercial collections | Discovery does not imply asset download rights, tile rendering, complete coverage, or current imagery |
| **OpenStreetMap / Nominatim** | CONNECTOR when provisioned | Geocoding, reverse geocoding, place and feature data | Public-service rate limits apply; no guaranteed business completeness, reviews, live traffic, or authoritative addressing |
| **OSRM / Valhalla** | CONNECTOR when provisioned | Road, walking, or cycling route computation, depending on deployed profiles | No guaranteed live traffic, public-transit schedules, or navigation-grade freshness |
| **Overpass API** | CONNECTOR when provisioned | Structured queries over OpenStreetMap features within a bounded area | Rate-limited; complex queries may time out; reflects OSM completeness and tagging quality |
| **OGC WMS / WFS / WMTS services** | CONNECTOR when provisioned | Agency or project raster maps, tiles, and vector features | Coverage, schema, licensing, freshness, authentication, and service reliability vary by provider |
| **CesiumJS or equivalent rendered globe** | BROWSER for visual observation; CONNECTOR only if a structured backend is separately verified | 2D/3D visualization of configured imagery, terrain, and overlays | A rendered globe is semantically opaque; pixel access does not establish feature identity, geology, ownership, or API access |
| **Google Maps Platform** | UNAVAILABLE by default; CONNECTOR only if explicitly provisioned and verified | Product-dependent maps, places, geocoding, routes, and imagery | Vendor credentials, terms, quotas, and product-specific APIs apply; browser viewing is not API access |
| **Google Earth Engine** | UNAVAILABLE by default; CONNECTOR only if explicitly provisioned and verified | Cloud geospatial analysis and supported remote-sensing catalogs | Requires authorized integration; catalog presence does not imply unrestricted export or use |
| **Google Street View** | UNAVAILABLE by default; CONNECTOR only if explicitly provisioned and verified | Street-level imagery where available | Coverage, capture date, licensing, credentials, and product restrictions apply |
| **Mapbox / Bing Maps / HERE / TomTom** | UNAVAILABLE by default; CONNECTOR only if explicitly provisioned and verified | Vendor-specific maps, geocoding, routes, traffic, and related services | Vendor lock-in, credentials, quotas, licensing, and product-specific coverage |
| **Training-data recall** | Not a capability source; claim ceiling is INT_SPATIAL | General non-live context about well-known places and spatial concepts | Not live, not reliably precise, may be stale or wrong, and never supports `OBS_SPATIAL` or `API_SPATIAL` |

---

## 7. Universal Pitfalls

1. **Configuration is not availability.** A registered tool, documented API, or prior successful call does not prove the connector is live and authorized now.
2. **Database knowledge is not query evidence.** Knowing that a source may contain a record is not the same as retrieving and validating that record.
3. **A screenshot is not API access.** Browser-rendered maps support only bounded visual observations, not programmatic geocoding, routing, feature lookup, or semantic inference.
4. **Health is not query success.** A healthy connector still requires a successful, validated query before location-specific `API_SPATIAL` claims are made.
5. **Rate limits can masquerade as empty data.** Empty or malformed responses may be throttling or error pages rather than valid “no result” answers.
6. **Authorization gates are not outages.** A reachable service that requests session initialization or authorization is gated, not dead; re-probe after approved authorization.
7. **Do not hammer failing services.** Back off after repeated failures or cooldown signals; disclose temporary unavailability.
8. **Precision must be earned.** Never convert a broad or ambiguous place reference into exact coordinates without verified resolution.
9. **Recall is not live spatial evidence.** Remembered coordinates, boundaries, routes, and current place attributes require verification before being stated as observations or API facts.
10. **Do not mix epistemic labels in one sentence.** Separate observed, derived, interpreted, and speculative claims so certainty is not laundered across them.
11. **Do not use visual surfaces for semantic questions.** A rendered map or globe cannot by itself identify a formation, legal boundary, ownership, current hazard, or route quality.
12. **Absence of evidence is not spatial evidence of absence.** Missing records may reflect sparse coverage, filters, resolution, indexing, or service failure.
13. **Coordinate order and reference systems matter.** Confirm latitude/longitude order, units, datum, axis conventions, and CRS before computing or comparing locations.
14. **Freshness is source-specific.** A query run now may still return an old dataset; report both query time and dataset date when available.
15. **Never imply global completeness.** Access to a bounded endpoint, catalog, layer, or vendor product does not establish coverage of the entire Earth or every available record.
