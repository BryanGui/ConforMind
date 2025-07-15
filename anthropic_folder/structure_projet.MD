# ConforMind-AI - Structure Projet
## Architecture EU AI Act - Multi-niveaux d'audit

├── anthropic_folder
│   ├── devellopement_phased.MD
│   ├── guide_complet.MD
│   ├── program_P1.MD
│   ├── Service_hybride.MD
│   └── structure_projet.MD
├── backend
│   ├── app
│   │   ├── api_schemas
│   │   │   ├── ai_models.py
│   │   │   ├── compliance.py
│   │   │   ├── file_storage.py
│   │   │   ├── health.py
│   │   │   ├── __init__.py
│   │   │   ├── reports.py
│   │   │   ├── sputil.py
│   │   │   └── user.py
│   │   ├── business_logic
│   │   │   ├── ai_analyzer.py
│   │   │   ├── analysis
│   │   │   │   ├── __init__.py
│   │   │   │   ├── performance_analyzer.py
│   │   │   │   └── risk_assessor.py
│   │   │   ├── bias_detector.py
│   │   │   ├── compliance_engine.py
│   │   │   ├── __init__.py
│   │   │   ├── report_generator.py
│   │   │   ├── reporting
│   │   │   │   ├── compliance_reporter.py
│   │   │   │   └── __init__.py
│   │   │   ├── scoring
│   │   │   │   ├── __init__.py
│   │   │   │   ├── model_scorer.py
│   │   │   │   ├── organization_scorer.py
│   │   │   │   ├── system_scorer.py
│   │   │   │   └── workflow_scorer.py
│   │   │   └── validation
│   │   │       ├── bias_validator.py
│   │   │       ├── documentation_checker.py
│   │   │       ├── eu_ai_act_checker.py
│   │   │       └── __init__.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── __init__.py
│   │   │   └── nace_database.py
│   │   ├── database_tables
│   │   │   ├── client_profile
│   │   │   │   ├── audit_info
│   │   │   │   │   ├── audit_info.py
│   │   │   │   │   ├── enums.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── audit_info.py
│   │   │   │   ├── basic_info
│   │   │   │   │   ├── basic_info.py
│   │   │   │   │   ├── enums.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── certification_info
│   │   │   │   │   ├── certification_info.py
│   │   │   │   │   ├── certification_list.json
│   │   │   │   │   ├── enums.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── utils.py
│   │   │   │   ├── governance_info
│   │   │   │   │   ├── enums.py
│   │   │   │   │   ├── governance_info.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── stakeholder_info
│   │   │   │   │   ├── enums.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── stakeholder_info.py
│   │   │   │   ├── stakeholder_info.py
│   │   │   │   ├── techstack_info
│   │   │   │   │   ├── cloud_providers.json
│   │   │   │   │   ├── crm_systems.json
│   │   │   │   │   ├── enums.py
│   │   │   │   │   ├── erp_systems.json
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── monitoring_tools.json
│   │   │   │   │   ├── techstack_info.py
│   │   │   │   │   └── utils.py
│   │   │   │   └── tech_stack_info.py
│   │   │   ├── compliance_report.py
│   │   │   ├── enum_compliances.py
│   │   │   ├── enums.py
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── user.py
│   │   ├── __init__.py
│   │   ├── routers
│   │   │   ├── ai_models.py
│   │   │   ├── auth.py
│   │   │   ├── compliance.py
│   │   │   ├── file_storage.py
│   │   │   ├── health.py
│   │   │   ├── __init__.py
│   │   │   ├── reports.py
│   │   │   └── router_models.MD
│   │   └── utilities
│   │       ├── auth_temp.py
│   │       ├── file_utils.py
│   │       ├── __init__.py
│   │       └── logger.py
│   ├── conformind_ai.egg-info
│   │   ├── dependency_links.txt
│   │   ├── PKG-INFO
│   │   ├── requires.txt
│   │   ├── SOURCES.txt
│   │   └── top_level.txt
│   ├── docs
│   └── tests
├── conformind_ai.db
├── conformind_ai.db-shm
├── conformind_ai.db-wal
├── data
│   ├── clients
│   ├── client_uploads
│   ├── demo_datasets
│   ├── generated_reports
│   ├── models
│   ├── processed_models
│   ├── reports
│   ├── temp_files
│   └── uploads
├── docs
│   ├── BiasDetectionGuide.MD
│   └── EvaluationGratuiteEUAIAct.MD
├── frontend
│   ├── public
│   └── src
├── main.py
├── PDF
│   ├── Audit Trail EU AI Act - Guide Complet Toutes Étapes.pdf
│   └── TODO MVP - Étape 1 Description Générale + Phases Suivantes.pdf
├── Pipfile
├── Pipfile.lock
├── pyproject.toml
├── README.md
├── requirements.txt
└── scripts
