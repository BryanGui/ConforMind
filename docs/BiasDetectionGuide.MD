# 🔍 Bias Detection Guide - ConforMind AI

## 📋 **Vue d'ensemble**

La détection de biais dans l'IA est **cruciale pour la conformité EU AI Act**. Un modèle biaisé peut entraîner des discriminations illégales et des amendes jusqu'à €35 millions.

---

## 👥 **GROUPES DE POPULATION À RISQUE**

### **📊 Variables Démographiques**

#### **1. 🎂 Âge**
- **Groupes à risque** : Seniors (>50 ans), Jeunes (<25 ans), Âge légal retraite
- **Biais typiques** : Discrimination embauche seniors, Exclusion crédit jeunes
- **Variables proxy** : Année naissance, Ancienneté emploi, Statut retraite

#### **2. 👫 Genre**
- **Groupes à risque** : Femmes, Hommes, Non-binaires, Transgenres
- **Biais typiques** : Écart salarial, Discrimination maternité, Exclusion tech/finance
- **Variables proxy** : Prénom, Titre (M./Mme), Congés parentaux, Secteur d'activité

#### **3. 🌍 Origine Raciale/Ethnique**
- **Groupes à risque** : Minorités ethniques, Populations immigrées, Origines géographiques
- **Biais typiques** : Red-lining bancaire, Discrimination embauche, Profilage racial
- **Variables proxy** : Nom/prénom, Code postal, Nationalité, Langue maternelle

#### **4. 📍 Localisation Géographique**
- **Groupes à risque** : Zones défavorisées, Banlieues, Zones rurales, Territoires d'outre-mer
- **Biais typiques** : Exclusion bancaire géographique, Tarification discriminatoire
- **Variables proxy** : Code postal, Région, Type habitat, Revenus médians zone

### **📋 Variables Socio-économiques**

#### **5. 💰 Niveau de Revenus**
- **Groupes à risque** : Bas revenus, Travailleurs précaires, Sans-emploi
- **Biais typiques** : Accès crédit limité, Services dégradés, Surprimes assurance
- **Variables proxy** : Salaire, Type contrat, Secteur d'activité, Patrimoine

#### **6. 🎓 Niveau d'Éducation**
- **Groupes à risque** : Sans diplôme, Autodidactes, Formations non-reconnues
- **Biais typiques** : Discrimination recrutement, Accès formation, Évolution carrière
- **Variables proxy** : Diplômes, École fréquentée, Compétences déclarées

#### **7. 💼 Statut Professionnel**
- **Groupes à risque** : Indépendants, Intérimaires, Secteurs "à risque"
- **Biais typiques** : Refus crédit, Tarification assurance, Accès services
- **Variables proxy** : Type contrat, Secteur, Ancienneté, Revenus variables

### **🏥 Variables de Santé**

#### **8. 🦽 Handicap**
- **Groupes à risque** : Handicap physique, Handicap mental, Maladies chroniques
- **Biais typiques** : Discrimination embauche, Exclusion assurance, Accessibilité
- **Variables proxy** : Congés maladie, Aménagements poste, Allocations handicap

#### **9. 🏥 État de Santé**
- **Groupes à risque** : Maladies chroniques, Troubles mentaux, Conditions génétiques
- **Biais typiques** : Surprimes assurance, Discrimination emploi, Exclusion services
- **Variables proxy** : Antécédents médicaux, Traitements, Arrêts maladie

### **👨‍👩‍👧‍👦 Variables Familiales**

#### **10. 💒 Situation Familiale**
- **Groupes à risque** : Familles monoparentales, Couples non-mariés, Familles nombreuses
- **Biais typiques** : Discrimination logement, Accès crédit, Mobilité professionnelle
- **Variables proxy** : État civil, Nombre enfants, Situation du conjoint

#### **11. 🤱 Parentalité**
- **Groupes à risque** : Femmes enceintes, Jeunes parents, Familles nombreuses
- **Biais typiques** : Discrimination embauche femmes, Évolution carrière, Flexibilité
- **Variables proxy** : Congés parentaux, Âge enfants, Garde d'enfants

### **🙏 Variables Idéologiques**

#### **12. ⛪ Religion**
- **Groupes à risque** : Minorités religieuses, Pratiquants visibles, Athées
- **Biais typiques** : Discrimination embauche, Accès services, Profilage sécuritaire
- **Variables proxy** : Nom/prénom, Jours fériés, Régime alimentaire, Tenue vestimentaire

#### **13. 🗳️ Opinions Politiques**
- **Groupes à risque** : Militants, Opposants, Abstentionnistes
- **Biais typiques** : Discrimination embauche, Surveillance, Exclusion sociale
- **Variables proxy** : Activités associatives, Réseaux sociaux, Adhésions

---

## 🏢 **SECTEURS IMPACTÉS PAR LE BIAIS**

### **🏦 Banking & Finance**
#### **Variables critiques :**
- **Âge** : Seniors discriminés crédit (>65 ans)
- **Genre** : Femmes pénalisées entrepreneuriat
- **Code postal** : Red-lining zones sensibles
- **Revenus** : Exclusion bas revenus, travailleurs précaires

#### **Cas d'usage à risque :**
- Scoring crédit automatique
- Assurance vie/emprunt
- Investissement/épargne
- Cartes de crédit

### **👥 Ressources Humaines**
#### **Variables critiques :**
- **Genre** : Biais recrutement tech/finance
- **Âge** : Discrimination seniors, jeunes diplômés
- **Origine** : Discrimination nom/accent
- **Parentalité** : Pénalisation femmes enceintes

#### **Cas d'usage à risque :**
- CV screening automatique
- Évaluation performances
- Promotion/évolution
- Formation recommandations

### **🏥 Santé & Médical**
#### **Variables critiques :**
- **Origine ethnique** : Sous-diagnostic minorités
- **Genre** : Biais douleur femmes
- **Âge** : Rationnement soins seniors
- **Statut social** : Accès soins différencié

#### **Cas d'usage à risque :**
- Diagnostic assisté IA
- Allocation ressources
- Recommandations traitement
- Priorisation urgences

### **⚖️ Justice & Sécurité**
#### **Variables critiques :**
- **Origine ethnique** : Profilage racial
- **Code postal** : Biais géographique
- **Âge** : Jeunes surreprésentés
- **Statut social** : Biais classe sociale

#### **Cas d'usage à risque :**
- Évaluation risque récidive
- Reconnaissance faciale
- Contrôles préventifs
- Sanctions automatiques

### **🎓 Éducation**
#### **Variables critiques :**
- **Origine sociale** : Reproduction inégalités
- **Genre** : Orientation STEM
- **Origine ethnique** : Attentes biaisées
- **Handicap** : Exclusion programmes

#### **Cas d'usage à risque :**
- Admission automatique
- Orientation scolaire
- Notation assistée
- Recommandations parcours

### **🏛️ Services Publics**
#### **Variables critiques :**
- **Origine** : Discrimination immigrés
- **Statut social** : Accès inégal
- **Localisation** : Déserts services
- **Handicap** : Accessibilité

#### **Cas d'usage à risque :**
- Allocations sociales
- Attribution logement
- Services administratifs
- Contrôles fiscaux

### **🛒 E-commerce & Marketing**
#### **Variables critiques :**
- **Genre** : Prix différenciés
- **Âge** : Ciblage générationnel
- **Revenus** : Discrimination tarifaire
- **Localisation** : Disponibilité services

#### **Cas d'usage à risque :**
- Pricing dynamique
- Recommandations produits
- Publicité ciblée
- Conditions de livraison

---

## ⚖️ **NIVEAUX D'ACCEPTATION ET SEUILS**

### **🚦 Classification ConforMind**

#### **✅ ACCEPTABLE (Pas de biais)**
- **Seuil** : Écart < 5%
- **Exemples** :
  - Approbation crédit : Hommes 78% vs Femmes 74% = 4% ✅
  - Embauche : Majorité 45% vs Minorité 42% = 3% ✅
- **Action** : Monitoring continu, pas d'action immédiate

#### **⚠️ MODÉRÉ (Surveillance requise)**
- **Seuil** : 5% ≤ Écart < 20%
- **Exemples** :
  - Scoring crédit : Jeunes 65% vs Seniors 50% = 15% ⚠️
  - Promotion : Hommes 30% vs Femmes 18% = 12% ⚠️
- **Actions requises** :
  - Investigation approfondie
  - Plan de mitigation 30 jours
  - Monitoring renforcé
  - Documentation justification

#### **❌ CRITIQUE (Non-conforme EU AI Act)**
- **Seuil** : Écart ≥ 20%
- **Exemples** :
  - Crédit immobilier : Blancs 80% vs Minorités 55% = 25% ❌
  - Recrutement tech : Hommes 70% vs Femmes 35% = 35% ❌
- **Actions obligatoires** :
  - Arrêt immédiat système
  - Audit complet modèle
  - Retraining obligatoire
  - Validation externe
  - Documentation légale

### **📊 Métriques de Mesure**

#### **1. Demographic Parity (Parité Démographique)**
```python
DemographicParity = |P(Y=1|A=0) - P(Y=1|A=1)|

Exemple Banking :
- Approbation Hommes : 75%
- Approbation Femmes : 60%
- Écart = |75% - 60%| = 15% → ⚠️ MODÉRÉ
```

#### **2. Equalized Odds (Égalité des Chances)**
```python
EqualizedOdds = |TPR_group0 - TPR_group1| + |FPR_group0 - FPR_group1|

Acceptable : < 0.10 (10%)
Modéré : 0.10 - 0.40 (10-40%)
Critique : > 0.40 (>40%)
```

#### **3. Calibration Error (Erreur de Calibration)**
```python
CalibrationError = |P(Y=1|Score=s, A=0) - P(Y=1|Score=s, A=1)|

Acceptable : < 0.05 (5%)
Modéré : 0.05 - 0.15 (5-15%)
Critique : > 0.15 (>15%)
```

### **🏦 Seuils Sectoriels Spécialisés**

#### **Banking/Finance (Plus strict)**
- **Acceptable** : < 3% (réglementation stricte)
- **Modéré** : 3% - 10%
- **Critique** : > 10%

#### **Justice/Police (Ultra-strict)**
- **Acceptable** : < 2% (droits fondamentaux)
- **Modéré** : 2% - 8%
- **Critique** : > 8%

#### **Marketing/E-commerce (Plus tolérant)**
- **Acceptable** : < 10% (impact commercial)
- **Modéré** : 10% - 30%
- **Critique** : > 30%

### **📈 Évolution Temporelle**

#### **Tendance Réglementaire :**
- **2025** : Seuils actuels
- **2026** : Durcissement -2% (EU AI Act plein effet)
- **2027+** : Convergence vers 2-3% maximum

#### **Monitoring Continu :**
- **Quotidien** : Systèmes critiques (justice, santé)
- **Hebdomadaire** : Systèmes haut risque (banking, RH)
- **Mensuel** : Systèmes risque limité

---

## 🎯 **Qu'est-ce que le Biais en IA ?**

### **Définition :**
Le biais survient quand un modèle IA produit des **résultats discriminatoires** systématiques contre certains groupes protégés (âge, genre, origine ethnique, etc.).

### **Exemple Concret - Crédit Bancaire :**
```
Modèle de scoring crédit :
- Hommes blancs 25-35 ans : 85% d'approbation
- Femmes même profil : 65% d'approbation  
- Personnes >50 ans : 45% d'approbation

➡️ BIAIS DÉTECTÉ : Discrimination par genre et âge
```

---

## ⚖️ **Types de Biais Détectés**

### **1. Biais Démographique (Demographic Parity)**
**Définition :** Taux de décisions positives inégal entre groupes

**Formule :**
```
Bias Score = |P(Decision=Positive | Group A) - P(Decision=Positive | Group B)|

Exemple :
- Approbation Hommes : 80%
- Approbation Femmes : 60% 
- Bias Score = |0.80 - 0.60| = 0.20 (20% d'écart)
```

**Seuil EU AI Act :** Écart > 5% = Biais significatif

### **2. Biais d'Égalité des Chances (Equalized Odds)**
**Définition :** Taux d'erreur différent selon les groupes

**Formule :**
```
Pour chaque groupe, même taux de :
- Vrais Positifs (Sensitivity)
- Vrais Négatifs (Specificity)

Exemple Banking :
- Hommes : 90% vrais positifs, 85% vrais négatifs
- Femmes : 75% vrais positifs, 80% vrais négatifs
➡️ Inégalité de performance = Biais
```

### **3. Biais de Calibration**
**Définition :** Scores de confiance incorrects selon les groupes

**Exemple :**
```
Score de risque 70% devrait signifier :
- 70% de chance de défaut pour TOUS les groupes
- Si Groupe A : 70% → 80% défaut réel
- Et Groupe B : 70% → 60% défaut réel
➡️ Modèle mal calibré = Biais
```

---

## 🚨 **Obligations EU AI Act**

### **Pour Systèmes Haut Risque (Banking/Crédit) :**

#### **1. Tests de Biais Obligatoires**
- ✅ Tests avant mise en production
- ✅ Monitoring continu en production
- ✅ Documentation des résultats
- ✅ Actions correctives si biais détecté

#### **2. Groupes Protégés à Tester**
- **Art. 7 EU AI Act** : Genre, âge, handicap, origine
- **GDPR** : Catégories spéciales de données
- **Législations nationales** : Protections additionnelles

#### **3. Documentation Requise**
- **Bias Impact Assessment** : Analyse préalable
- **Mitigation Measures** : Actions de correction
- **Monitoring Plan** : Surveillance continue
- **Audit Trail** : Traçabilité des tests

---

## 🛠️ **Implémentation ConforMind**

### **Pipeline de Détection :**
```python
# 1. Chargement modèle et données test
model = load_model(model_path)
test_data = prepare_test_data()

# 2. Prédictions par groupe
predictions = model.predict(test_data)
groups = identify_protected_groups(test_data)

# 3. Calcul métriques de biais
bias_metrics = {
    'demographic_parity': calculate_demographic_parity(predictions, groups),
    'equalized_odds': calculate_equalized_odds(predictions, groups),
    'calibration': calculate_calibration(predictions, groups)
}

# 4. Classification sévérité
severity = classify_bias_severity(bias_metrics)

# 5. Recommandations
recommendations = generate_mitigation_strategies(bias_metrics)
```

### **Output ConforMind :**
```json
{
    "bias_detected": true,
    "severity": "medium",
    "affected_groups": ["female", "senior"],
    "metrics": {
        "demographic_parity": 0.15,
        "equalized_odds": 0.08,
        "calibration_error": 0.12
    },
    "eu_ai_act_compliance": "NON_COMPLIANT",
    "recommendations": [
        "Implement demographic parity constraint",
        "Retrain with balanced dataset",
        "Add fairness regularization"
    ]
}
```

---

## 📚 **Références et Standards**

### **Réglementations :**
- **[EU AI Act - Article 10](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)** : Data governance et biais
- **[ISO/IEC 23053:2022](https://www.iso.org/standard/74438.html)** : Framework for AI risk management
- **[IEEE 2857-2021](https://standards.ieee.org/ieee/2857/7273/)** : Privacy engineering for AI

### **Standards Techniques :**
- **[Fairlearn Documentation](https://fairlearn.org/)** : Microsoft framework
- **[AI Fairness 360](https://aif360.mybluemix.net/)** : IBM toolkit
- **[What-If Tool](https://pair-code.github.io/what-if-tool/)** : Google analysis tool

### **Papers de Référence :**
- **Dwork et al. (2012)** : "Fairness through awareness"
- **Hardt et al. (2016)** : "Equality of opportunity in supervised learning"
- **Chouldechova (2017)** : "Fair prediction with disparate impact"

### **Banking/Finance Spécifique :**
- **[ECOA (Equal Credit Opportunity Act)](https://www.consumerfinance.gov/compliance/compliance-resources/lending-rules/equal-credit-opportunity-act/)** : US credit discrimination law
- **[FCA ML Guidance](https://www.fca.org.uk/publications/finalised-guidance/fg21-1-guidance-firms-use-artificial-intelligence)** : UK financial AI guidance
- **[ECB AI Guide](https://www.bankingsupervision.europa.eu/press/pr/date/2021/html/ssm.pr210618~f3d04c7ac0.en.html)** : European banking AI supervision

---

## 🔧 **Outils de Détection**

### **Libraries Python :**
```python
# Fairness metrics
from fairlearn.metrics import demographic_parity_difference
from aif360.metrics import BinaryLabelDatasetMetric

# Statistical tests
from scipy.stats import chi2_contingency
from statsmodels.stats.proportion import proportions_ztest

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
```

### **Datasets de Test :**
- **Adult/Census Income** : Classification benchmark
- **COMPAS Recidivism** : Criminal justice fairness
- **German Credit** : Credit approval fairness
- **Bank Marketing** : Marketing response fairness

---

## ⚡ **Actions Correctives**

### **Si Biais Détecté :**

#### **1. Pre-processing (Données)**
- ✅ **Re-sampling** : Équilibrer les groupes
- ✅ **Feature engineering** : Supprimer variables proxy
- ✅ **Synthetic data** : Générer données équilibrées

#### **2. In-processing (Entraînement)**
- ✅ **Fairness constraints** : Pénaliser le biais
- ✅ **Adversarial debiasing** : Réseaux antagonistes
- ✅ **Multi-objective optimization** : Précision + fairness

#### **3. Post-processing (Prédictions)**
- ✅ **Threshold optimization** : Seuils par groupe
- ✅ **Calibration** : Ajuster scores de confiance
- ✅ **Output modification** : Correction directe

### **Monitoring Continu :**
```python
# Alertes automatiques
if bias_score > threshold:
    send_alert("Bias detected in production model")
    trigger_model_review()
    log_incident(model_id, bias_metrics)
```

---

## 🎯 **Checklist Conformité**

### **✅ Pre-deployment :**
- [ ] Bias testing sur dataset de validation
- [ ] Documentation Bias Impact Assessment
- [ ] Approval équipe légale/compliance
- [ ] Plan de monitoring défini

### **✅ Production :**
- [ ] Monitoring automatique actif
- [ ] Alertes configurées
- [ ] Audit trail des prédictions
- [ ] Review périodique (mensuel/trimestriel)

### **✅ Incident Response :**
- [ ] Procédure si biais détecté
- [ ] Escalation vers équipe légale
- [ ] Plan de mitigation défini
- [ ] Communication stakeholders

**Cette documentation couvre tous les aspects du bias detection pour ConforMind ! 🚀**