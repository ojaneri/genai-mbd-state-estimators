# Physics-Guided Generative AI for automotive state estimation — code, results and preregistrations

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23190824.svg)](https://doi.org/10.5281/zenodo.23190824)

Companion repository of the paper *"Physics-Guided Generative AI for Automotive State Estimation and Embedded Deployment"* (Rafael Santos Dominguez, Osvaldo Janeri Filho, Jeferson José de Lima, Max Mauro Dias Santos; Federal Technological University of Paraná — Ponta Grossa).

It contains everything behind Section V of the paper (evaluation of the generative stage on public data) and the
context-gating test of Section IV. The OEM data, the Simulink model and the in-vehicle code of the fuel-level case study
are confidential and are **not** included; the bench-measured tank curves are reproduced from the thesis (see below).

## Contents

| Path | What |
|---|---|
| `experiments/data_reduction/run3.py` | Main experiment: data-reduction protocol, generators, physical audits, physics-structured models, hybrids, utility gate (`--auto-select`), fidelity scores. Domains: `fuel`, `battery`, `bess_temp`. |
| `experiments/data_reduction/run.py`, `run2.py` | Earlier rounds (TimeGAN round 1, generator grid of round 2). |
| `experiments/data_reduction/gens.py`, `timegan.py`, `timevae.py` | Generators: DDPM (1-D), TimeGAN, recurrent VAE, VAR, block bootstrap. |
| `experiments/data_reduction/tools/convert_*.py` | Converters of the public datasets to the common input format. |
| `experiments/data_reduction/tools/cross_domain.py` | Cross-domain table and figure → `cross_domain.json`, `cross_domain.pdf`. |
| `experiments/data_reduction/tools/paper_figs.py` | Evidence figures and tables: per-seed changes, battery curves, gate choices, fidelity vs. utility, statistics (95% CI, effect size), audit tiers, data equivalence, distance to the all-data model, per-channel detectability. |
| `experiments/data_reduction/tools/battery_table.py`, `gate_summary.py`, `fid_vs_utility.py`, `analyze_d0030.py` | Battery candidates table, utility-gate summary, fidelity–utility correlation, preregistered analysis of round 11. |
| `experiments/data_reduction/tools/fig_curve.py`, `fig_vf_curves.py` | Vehicle-1 learning curve; Fig. 2 (tank curves). |
| `experiments/data_reduction/desktop_results/Jxxx/` | Per-job outputs: `results.json` (every seed, fraction and variant), logs, `REPORT.md`. |
| `experiments/opel_refuel/` | Context gating of refuel detection (Opel and Itabira), with results. |
| `data/thesis_vf_curves/` | Resistance-to-volume curves of 24 tanks and envelopes, from the thesis appendix (CC BY 4.0). |
| `PREREGISTRATION.md` | Hypotheses, outcomes and decision rules recorded before each run (d-0005 – d-0033). |
| `REPRODUCE.md` | The exact command of every job J001–J035c. |

Job ↔ paper: vehicle 1 (Opel) J009, J012, J014, J015, J016, J017, J018, J019, J024, J026, J031; vehicle 2 (Itabira) J013,
J025, J028; battery cell (LG 18650HG2) J020b, J021, J022, J023, J027, J029, J030; field BESS SOC J032b, J033b, J034b;
BESS cell temperature J035c; round 11 (d-0030, d-0032, d-0033): J038 (MLP, seeds 3–4), J039 and J040 (bootstrap controls for vehicle 2 and BESS temperature), J044 (failed, see its report; re-run as J044r); TimeGAN round 1 `desktop_results/20260930-2207`. Jobs J036, J037, J041–J043 and J044r are queued and will be added in a later version. Jobs with a later letter (J020→J020b,
J032→J032b, …) replace failed runs; the failure reports are kept.

## Data (not redistributed — download from the sources)

| Domain | Dataset | Licence |
|---|---|---|
| Vehicle 1 | Opel Corsa 2012 OBD-II, Kaggle `pedro2025/obd2-panel-opel-2012` (`dataset.csv`, `refueling_history.csv`); the file changed on Kaggle after our download — see the note at the end of `PREREGISTRATION.md` | CC BY 4.0 |
| Vehicle 2 | Itabira OBD-II, Kaggle `brunops2/obd-2-vehicular-dataset-trace` → `tools/convert_itabira.py` | CC0 |
| Battery cell | LG 18650HG2, Mendeley Data doi:10.17632/cp3473x7xv.3 → `tools/convert_lghg2.py` | CC BY 4.0 |
| Field BESS | Qu, Zenodo doi:10.5281/zenodo.20094787 → `tools/convert_bess.py` (SOC mode; `temp` mode for cell temperature) | CC BY 4.0 |

Expected SHA-256 of the converted files are given in `REPRODUCE.md`.

## Running

Python ≥ 3.10; `pip install -r requirements.txt`. The jobs ran on one NVIDIA RTX 3060 (PyTorch with CUDA); a DDPM job
takes 2–8 h. Example (vehicle 1, pre-registered replication, Table III):

    cd experiments/data_reduction
    python -u run3.py ../data out/J012 --gen ddpm --iters 50000 --hidden 128 --dequant --post quant --seeds 5,6,7,8,9 --fracs 0.01,0.02,0.05,0.1

Regenerate Table III / Fig. 4 from the archived results (from the repository root):

    python experiments/data_reduction/tools/cross_domain.py cross_domain.pdf

GPU training is not bit-for-bit deterministic; reruns with the same seeds differ slightly (e.g. J013 vs J025).

Code comments and internal reports are in Portuguese.

## Licences

Code: MIT (`LICENSE`). Results, reports, pre-registration records and the tank-curve tables: CC BY 4.0
(`LICENSE-RESULTS`); the tank curves come from R. S. Dominguez, *Supervised Machine Learning Applied to Fuel Level
Measurement in Passenger Vehicles*, MEng thesis, UTFPR, 2026 (CC BY 4.0).

## Citation

See `CITATION.cff`. Please cite the paper and this archive: doi:10.5281/zenodo.23190824 (all versions; v1.0.0: doi:10.5281/zenodo.23190825).

## Acknowledgment

This study was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior — Brasil (CAPES).
Generative AI tools (Claude, Anthropic) were used to assist in writing and checking the analysis scripts; the authors
reviewed all content and take full responsibility for it.
