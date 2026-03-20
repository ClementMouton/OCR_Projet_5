from pydantic import BaseModel, Field


class EmployeeInput(BaseModel):
    age: int = Field(..., ge=0)

    genre: str

    revenu_mensuel: float = Field(..., ge=0)

    statut_marital: str
    departement: str
    poste: str

    nombre_experiences_precedentes: int = Field(..., ge=0)

    nombre_heures_travailless: int = Field(..., ge=0) 

    annee_experience_totale: int = Field(..., ge=0)
    annees_dans_l_entreprise: int = Field(..., ge=0)
    annees_dans_le_poste_actuel: int = Field(..., ge=0)

    satisfaction_employee_environnement: int = Field(..., ge=0, le=5)

    note_evaluation_precedente: int = Field(..., ge=0, le=5)

    niveau_hierarchique_poste: int = Field(..., ge=0)

    satisfaction_employee_nature_travail: int = Field(..., ge=0, le=5)
    satisfaction_employee_equipe: int = Field(..., ge=0, le=5)
    satisfaction_employee_equilibre_pro_perso: int = Field(..., ge=0, le=5)

    note_evaluation_actuelle: int = Field(..., ge=0, le=5)

    heure_supplementaires: str

    augementation_salaire_precedente: str 

    nombre_participation_pee: int = Field(..., ge=0)
    nb_formations_suivies: int = Field(..., ge=0)

    nombre_employee_sous_responsabilite: int = Field(..., ge=0)

    distance_domicile_travail: int = Field(..., ge=0)

    niveau_education: int = Field(..., ge=0)

    domaine_etude: str

    ayant_enfants: str

    frequence_deplacement: str

    annees_depuis_la_derniere_promotion: int = Field(..., ge=0)

    annes_sous_responsable_actuel: int = Field(..., ge=0) 