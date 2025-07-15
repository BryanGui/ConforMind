# 🤖 Router Models - Explication Détaillée

## 🎯 **À quoi sert ce router ?**

Le router `models.py` gère **tout le cycle de vie des modèles IA** que les clients veulent analyser pour la conformité EU AI Act.

## 👥 **Qui utilise ce router ?**

### **Utilisateurs finaux (clients) :**
- **Banques** : Upload modèles de crédit scoring
- **Assurances** : Upload modèles de tarification 
- **RH** : Upload modèles de recrutement automatique
- **Hôpitaux** : Upload modèles de diagnostic IA

### **Exemple concret d'usage :**
```
🏦 BNP Paribas veut vérifier son modèle de crédit
1. Data Scientist upload "credit_model.pkl" 
2. ConforMind analyse le modèle
3. Retourne : "HIGH_RISK - EU AI Act Article 6 applicable"
4. Génère rapport de conformité
```

## 🔄 **Workflow utilisateur complet**

### **Étape 1 : Upload du modèle**
```bash
# Le client upload son modèle via notre interface
POST /api/models/upload
- Fichier: credit_scoring_v2.pkl
- Use case: "credit_scoring" 
- Description: "Modèle XGBoost pour prêts particuliers"
```

### **Étape 2 : Analyse automatique**
```python
# Notre système analyse automatiquement :
- Type de modèle (XGBoost, Random Forest, etc.)
- Features utilisées (âge, sexe, salaire...)
- Classification EU AI Act (HIGH_RISK car crédit)
- Détection biais potentiels
```

### **Étape 3 : Consultation résultats**
```bash
# Le client peut consulter :
GET /api/models/1  # Détails du modèle
GET /api/compliance/1/analyze  # Analyse conformité  
GET /api/reports/1/pdf  # Rapport PDF
```

## 📊 **Types de modèles supportés**

### **Formats de fichiers :**
- **.pkl** : Scikit-learn, XGBoost (pickle Python)
- **.joblib** : Scikit-learn optimisé
- **.h5** : TensorFlow/Keras 
- **.onnx** : Format interopérable

### **Use cases détectés :**
- **credit_scoring** → HIGH_RISK (EU AI Act Article 6)
- **recruitment** → HIGH_RISK (discrimination interdite)
- **medical_diagnosis** → HIGH_RISK (sécurité patients)
- **chatbot** → LIMITED_RISK (transparence requise)
- **fraud_detection** → MINIMAL_RISK (généralement OK)

## 🏗️ **Architecture technique**

### **Ce router fait :**
1. **Réception** : Upload fichier client
2. **Validation** : Format supporté ?
3. **Stockage** : Sauvegarde sécurisée
4. **Analyse** : Extraction métadonnées
5. **Classification** : EU AI Act risk level
6. **Retour** : Confirmation + ID modèle

### **Ce router NE fait PAS :**
- ❌ Analyse de conformité détaillée (→ `compliance.py`)
- ❌ Génération rapports PDF (→ `reports.py`)
- ❌ Détection de biais (→ `services/bias_detector.py`)

## 💼 **Exemples concrets d'entreprises**

### **Banque Crédit Agricole :**
```python
# Upload modèle scoring crédit immobilier
{
  "name": "mortgage_scoring_2024.pkl",
  "use_case": "mortgage_approval", 
  "description": "Modèle XGBoost prêts immobiliers",
  "features": ["income", "age", "loan_amount", "employment_type"]
}
# → Classification: HIGH_RISK
# → EU AI Act: Article 6 applicable  
# → Human oversight requis
```

### **AXA Assurance :**
```python
# Upload modèle tarification auto
{
  "name": "car_insurance_pricing.pkl",
  "use_case": "insurance_pricing",
  "description": "Random Forest tarifs assurance auto", 
  "features": ["age", "car_model", "location", "driving_history"]
}
# → Classification: LIMITED_RISK
# → Transparence algorithme requise
```

### **Société Générale RH :**
```python
# Upload modèle tri CV automatique  
{
  "name": "cv_screening_model.h5",
  "use_case": "recruitment_screening",
  "description": "Deep Learning tri CV candidats",
  "features": ["education", "experience", "skills", "university"]
}
# → Classification: HIGH_RISK
# → ATTENTION: Biais discrimination potentiel
# → Audit approfondi requis
```

## 🔐 **Sécurité & Confidentialité**

### **Données sensibles :**
- **Modèles clients** = propriété intellectuelle
- **Features** = peuvent révéler stratégie business
- **Datasets** = données personnelles potentielles

### **Mesures sécurité :**
- **Stockage isolé** par client
- **Pas d'accès aux données** (juste métadonnées)
- **Suppression automatique** après analyse
- **Logs audit** : qui a uploadé quoi quand

## 🚀 **Évolution prévue**

### **Phase 1 (MVP) :**
- Upload modèles simples
- Classification basique EU AI Act
- Stockage local

### **Phase 2 (SaaS) :**
- Multi-tenant (isolation clients)
- Chiffrement end-to-end
- API rate limiting
- Authentification OAuth

### **Phase 3 (Enterprise) :**
- On-premise deployment
- Integration LDAP/SSO
- Custom compliance rules
- Advanced monitoring

## ❓ **Questions fréquentes**

**Q: Les clients peuvent voir les modèles des autres ?**
A: Non, isolation totale par client (multi-tenant)

**Q: ConforMind accède aux données d'entraînement ?**  
A: Non, juste au modèle (pas aux datasets)

**Q: Que se passe-t-il après upload ?**
A: Analyse auto → Classification risque → Rapport conformité

**Q: Formats non supportés ?**
A: Conversion ou export vers .pkl/.onnx recommandé