---
type: index
created: 2026-03-21
updated: 2026-03-21
tags: [genealogy, family-history]
---

# Genealogy Index

Master index for family history research, genetic ancestry, and digitized archives.

## Ancestry Research System

| Layer | File | Description |
|---|---|---|
| Family Tree | [[Family_Tree]] | Complete merged tree (all lines) |
| Research Log | [[Research_Log]] | Chronological record of research actions and findings |
| Open Questions | [[Open_Questions]] | Research gaps ranked by priority |
| Data Inventory | [[Data_Inventory]] | All source files tagged by type and reliability |
| Timeline | [[Timeline]] | Every dated event, ordered chronologically |

## Regions (Geographic Deep Dives)

| Region | Families | Genetic Signal |
|---|---|---|
| [[Slovakia]] | Kruppa, Szeles, Benyitzki, Farkas, Spireng, Matko | 25% Central European |
| [[North_Carolina]] | Wood, Arnold, Brooks, Almond, Moye, Briley, Carson | 50% British Isles |
| [[Virginia]] | Dubberly, Marshall, Ball, Tuggle, Brooks, Gwaltney | Colonial Roots |
| [[Georgia]] | Waters, Green, Moye | 19th Century Migration |
| [[Florida]] | Waters, Jones | Modern Branch |

## Surnames (Origin Research)

| Surname | Origin | Notes |
|---|---|---|
| [[Wood]] | UK | Main paternal line |
| [[Kruppa]] | Slovakia | Genetic branch (Stankovany) |
| [[Szeles]] | Slovakia | Genetic branch (Debraď) |
| [[Brooks]] | Wales/DE | Maternal branch (Ashe County) |
| [[Almond]] | Virginia | Maternal branch (Stanly County) |
| [[Waters]] | GA/FL | Maternal branch (Bulloch County) |
| [[Moye]] | VA/NC | Maternal branch (Pitt County) |

## Source Collections

| Collection | Files | Source | Status |
|---|---|---|---|
| GEDCOM | [[sources/Wood Family Tree.ged]] | Ancestry.com | Integrated |
| Obituaries | [[sources/Obituary information for Rose Mary Jones.html]] | Tributes.com | Transcribed |
| Vital Records | [[sources/jeremy_wood_birth_certificate.pdf]] | Wake County | Logged |

## File Locations

- **Originals (scans)**: `C:\Users\jerem\Documents\Wood_Family_History\sources\`
- **Vault (notes, transcriptions)**: `C:\Users\jerem\Documents\Wood_Family_History\`
- **Genomics**: `C:\Users\jerem\Documents\Wood_Family_History\sources\Jeremy_Wood_ancestry_composition_0.5.csv`

## Processing Pipeline

OCR toolchain: Tesseract + ocrmypdf + ImageMagick + Claude multimodal

### Document Classification

| Category | Description | OCR Method |
|---|---|---|
| photo_only | Portraits, group photos, buildings | Catalog only |
| printed_text | Certificates, newspaper clippings, diplomas | ocrmypdf (Tesseract) |
| handwritten | Record books, letters, funeral notes | Claude multimodal |
| mixed | Postcards (front/back), annotated docs | Layered approach |
