def find_fraudelant_data(patient_data):
    '''
    Find fraud claims based on repeated billing codes
    Args:
        patient_data (dict) : A dictionary containing claim details of patients
    Returns:
        list: A list of fraud claims    
    '''
    fraud_claims = []
    billing_code_count = {}
    for patient in patient_data.get('patients'):
        for claim in patient.get('claims'):
            billing_code = claim.get('billingCode')
            if not billing_code_count.get(billing_code):
                billing_code_count[billing_code]=[]
            billing_code_count[billing_code].append(claim) 
    if len(billing_code_count[billing_code]) > 1 :
        fraud_claims.extend(billing_code_count[billing_code])   

    return fraud_claims

def find_first_unique_claim(patient_data):
    billing_code_count = {}
    for patient in patient_data.get('patients'):
        for claim in patient.get('claims'):
            if claim.get('billingCode') not in billing_code_count :
                billing_code_count[claim.get('billingCode')] = 1
            else:
                billing_code_count[claim.get('billingCode')] += 1

        for claim in patient.get('claims'):
            if  billing_code_count[claim.get('billingCode')] == 1:
                return claim       

    

patient_data = {
    "patients": [
        {
            "id": "P001",
            "claims": [
                {
                    "id": "C001",
                    "amount": 100,
                    "billingCode": "B001",
                    "date": "2024-01-01"
                },
                {
                    "id": "C002",
                    "amount": 200,
                    "billingCode": "B001",
                    "date": "2024-01-05"
                },
                {
                    "id": "C003",
                    "amount": 150,
                    "billingCode": "B002",
                    "date": "2024-01-10"
                },
                {
                    "id": "C004",
                    "amount": 300,
                    "billingCode": "B001",
                    "date": "2024-04-05"
                }
            ]
        }
    ]
}


if __name__ == "__main__":
    # fraud_claims = find_fraudelant_data(patient_data)
    # print(fraud_claims)
    claim = find_first_unique_claim(patient_data)
    print(claim)