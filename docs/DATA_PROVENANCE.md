# Data Provenance, Source Registry & Verification Protocol

## 1. Authoritative Source Registry
The system strictly relies on official government records, ministerial releases, regulatory public notices, and verified school documentation:

| Source ID | Registry Name | Authority / Publisher | Source Type | URL Reference |
|---|---|---|---|---|
| `SRC_DGCA_PORTAL` | DGCA Official Portal | Directorate General of Civil Aviation | Official Regulator | [https://www.dgca.gov.in/](https://www.dgca.gov.in/) |
| `SRC_MOCA_FTO_8479` | MoCA FTO & DGCA Process | Ministry of Civil Aviation, GoI | Official Ministry | [https://www.civilaviation.gov.in/en/node/8479](https://www.civilaviation.gov.in/en/node/8479) |
| `SRC_MOCA_FTO_4635` | MoCA FTO Directory | Ministry of Civil Aviation, GoI | Official Ministry | [https://www.civilaviation.gov.in/node/4635](https://www.civilaviation.gov.in/node/4635) |
| `SRC_DGCA_DIGIGOV` | DGCA DigiGOV Portal | DGCA DigiGov Portal | Official Portal | [https://www.dgca.gov.in/digigov-portal/](https://www.dgca.gov.in/digigov-portal/) |
| `SRC_PIB_RANKING_2026` | PIB FTO Ranking Notice | Press Information Bureau / MoCA | Press Release | [https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255276&lang=1&reg=3](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255276&lang=1&reg=3) |
| `SRC_DGCA_RANKING_FRAMEWORK` | DGCA Ranking Framework Notice | DGCA Notice 30 Sept 2025 | Regulatory Notice | [https://www.dgca.gov.in/digigov-portal/Upload?attachId=OXOBBPO50KNsVklXF1f0cQ%3D%3D&baseLocale=en_US&flag=iframeAttachView](https://www.dgca.gov.in/digigov-portal/Upload?attachId=OXOBBPO50KNsVklXF1f0cQ%3D%3D&baseLocale=en_US&flag=iframeAttachView) |
| `SRC_DGCA_REGULATIONS` | DGCA Aviation Regulations Portal | DGCA Aviation Regulations | CARs & Circulars | [https://www.dgca.gov.in/digigov-portal/?page=aviation-regulations](https://www.dgca.gov.in/digigov-portal/?page=aviation-regulations) |
| `SRC_DGCA_DASHBOARD` | DGCA Official Operational Dashboard | DGCA Analytics Section | Official Dashboard | [https://www.dgca.gov.in/digigov-portal/webHP?actionVal=loadDashboard&requestType=ApplicationRH&screenId=11000188](https://www.dgca.gov.in/digigov-portal/webHP?actionVal=loadDashboard&requestType=ApplicationRH&screenId=11000188) |

---

## 2. Field-Level Provenance & Observations
To maintain data integrity and comply with academic business analytics guidelines:
- Every material field is backed by an observation record in `source_observations` linked via foreign key to `data_sources`.
- Attributes recorded per field:
  - `source_id`: Reference to authoritative entity.
  - `observed_value`: Exact string or numeric capture.
  - `observation_date`: Date the data was published by the authority.
  - `retrieval_date`: Date recorded into the database.
  - `verification_status`: `official_verified`, `school_published`, `estimated`, or `unverified`.
  - `confidence_score`: Metric from 0.0 to 1.0 reflecting publisher authority.

---

## 3. Disclosures & Handling of Missing / Unverified Data
- **Missing Data Policy**: Missing values (such as unbundled hostel charges or undisclosed multi-engine hourly rates) are NEVER imputed as zero. They are explicitly marked with `null`, and flagged in `missing_information` in recommendation reports.
- **Fees**: Broken down into verified inclusions (e.g. 200 hours flying, ground theory, simulator sessions) vs. exclusions (hostel accommodation, mess food, DGCA exam fees, flight test examiner fees).
- **Synthetic Data Isolation**: Where statistical demonstrations (e.g. logistic regression isolated demonstration mode) require augmented training samples, records are tagged with `is_synthetic: true` and segregated from verified regulatory facts.
