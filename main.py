import requests

headers = {
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Content-Length": "306",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "www.myhcgym.com",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; sdk_gphone_x86_64 Build/RSR1.201211.001)"
}

def main():
    print("#########################################################################################")
    print("Action: Open the application.")
    try:
        print("GET request to https://www.gymcompany.com/notificacoes/ping")
        url = "https://www.myhcgym.com/notificacoes/ping"
        response = requests.get(url)
        response.raise_for_status()
        print("GET request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("GET request failed:", e)

    print("#########################################################################################")
    print("Action: Loading dashboard.")
    try:
        print("POST request to https://www.gymcompany.com/notificacoes/showNotif")
        url = "https://www.myhcgym.com/notificacoes/showNotif"
        body = {
            "x": "AgHXwCU6KJIus4Ls4tSCTmMALUcmJP2FmFZUTANnuOSBiI9GQLTCsrLcY0Fz tXu4TsEbQVHLpRcuVZEcA/yCKqgNhZj1Y4A/1mms1aIAiZr0mxBGDuW4vg5Sgc5B2mRQrRsWSQA7Bqyw028/QShZm2y5G0nGgHMjpiqpDjpGrtpd CvoUkgX8//CdDC44pn0lyfpB1cdV/8C8sFfiptlIGulRnjSiZ7u EkvaEbGH9qS2//wZLFv1aJg0D6EtctaGlB/wXoolO1lxFkkRCdak5YyeaUmpW3BIOZtWIAFmDicw=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    try:
        print("POST request to https://www.gymcompany.com/lotacoesweb/showlotacoesweb")
        url = "https://www.myhcgym.com/lotacoesweb/showlotacoesweb"
        body = {
            "x": "AgH4CmfOX3lcS0u/MzdjdgZsKqe3KxVKqYBzdG/C5QiD/OA6FkOz8EpxDwzrcU51bXLPvBQX9M6/mVxrDkZizS A qKZUN1CLA4LOppBeWvsVj4IJNOF7Y3bgjR8hDJ vPofThX1JA33jMvFxPVIGmmQmtPq Tfie7C q2wovRBr9NpNcIktQhbdSjIDbrYOtzEJQ5SSXwhU4s FK8JCdogNwa9ALkBFdklNA6zNwDwuDPzHv4Uv5kluOti6QOCnHsTUmJ2bOlr2tdcVKKuDpH /GkEPBhJnGQs FxXYibmMPQ=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    try:
        print("POST request to https://www.gymcompany.com/planoaulas/showreservasaulas")
        url = "https://www.myhcgym.com/planoaulas/showreservasaulas"
        body = {
            "x": "AgGCGsb20i92XOgOHdEtPOkroNVLlllvk7SvEZ GmqTy2U4DiCDG0mqXgoligRemQcTfi7EKquMnTF8AVym1N5e23b6bLPVJKIbl1djSq6SCbhDZ7ThwnU2lEuXD0icQPBy6EraZ jsxqWOXQWLayaVvAn4HXXeLR16JE5OcVUXHupDaVpbBNO9p14gPG9wdW9TaIjlksxfm1hBuJgm77R9SX 2El94iNinmCwN8uD/f1q18EDrBQU0d43DKknq2EXHvt3dJoc1q9t/QABw077Pcz5  i BzrSk3/MQLbNAsr/jgXdWI6uG622HdkmKORaw="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    try:
        print("POST request to https://www.gymcompany.com/planoaulas/showavaliacoesaulas")
        url = "https://www.myhcgym.com/planoaulas/showavaliacoesaulas"
        body = {
            "x": "AgGBYSoib8F5LApWgFMqykU Gj9SaLN3W1SwDbFD3MxUeCU/gLVMAV yz0AHQiYSt1ZlnUNI/i0A vZejoq5mEi98xGrhrhg7hzXIY/OnW8 bFaVLOwDnYK7RK3j18scarYA/BugO7Voi/3fpkYfjY9Px1UsdNSAgFhga13ynZVin5c73m2l/xDKYGLagE4/XeDxdzOcdcShIePp7cde29fVh/DgQzHo5hTgVtutop0 Ln1h/oIs5JZtQBzDHpPllgLAlTnJ LKtCrkAsLCY Q89DOUR10ujS0Rss3nQ/N4bRQ=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    try:
        print("POST request to https://www.gymcompany.com/ppwebservice/downloadvideospt")
        url = "https://www.myhcgym.com/ppwebservice/downloadvideospt"
        body = {
            "x": "AgFWOO7VFgRq46yEgGIo0qq4Oqb0Czik9K16ud3FHI07ePY8X7pgMJgxenrmDl lmdnNayALjDqVrTLfGyGvz4g1krIuSXz4m6Yfy/cQVQcPVSKz35/YODHYIOxUDCmIyuOOUbE 2BIV/5g1 956Tqlxt5sxsRXDRYEfLYdm0zZQebkocT5F7O5UIRTUyO/BNJM="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    print("#########################################################################################")
    print("Action: Access the meal plan.")
    try:
        print("POST request to https://www.gymcompany.com/planoalimentar/getimageslistnut")
        url = "https://www.myhcgym.com/planoalimentar/getimageslistnut"
        body = {
            "x": "AgE5nxR868Ra2pClUZkrmfKcxmnGtgbnjK/NxQD6/yQaUk3oW8F1H6PnZEBv7dHD/y4fOUWja2yj16ykOhs6Z08IBeL9y5eNjqxLATcS/XNsn0YyQ8GS63v7UWf63Wsa4piOzEx3U6HQWwxGkVLbDgyw1NU4Jm42Q c6huuo/vdNbrDEAf5ULeXHofkwVPYkb5ulP6qQZyOAK1uCJzo0Iaf6wRTRzPWZd nHbJRkEes9czYeghFSXF0nYe /vE5XV7n3SrFqj9f7PJQp1APKApeF0dspRAYHTFf/mOTqtyE0mg=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    try:
        print("POST request to https://www.gymcompany.com/planoalimentar/showpalim")
        url = "https://www.myhcgym.com/planoalimentar/showpalim"
        body = {
            "x": "AgEkdryDIdHOSH/VVDO1q2OuWazql59XZOlF4ky6F8F68cVnvviPMUvdmosJLRBCKP9tvi2mEd5ppPnesJ J84BdyRIIVNCH3IU3iBEbFZluCHGrZegtQ7MsH6 mgh5gjQuU6zQzTMTXXRyGpyaKYHmV0b5nRkkHwY5EVpWrBuI0iABQozC765Ml/CZ4/ePT0kpmQbuakjh8rfK6Jg2jWvODLdNngHSulKwyr3S8IaTRX 84cBRo3Zh5bJyzQu4eor0cFPjPcJmcbQqeyF8ifo9fJxWeSCUN Qq7Cw1E2NIdIQ=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    print("#########################################################################################")
    print("Action: Book a class.")
    try:
        print("POST request to https://www.gymcompany.com/planoaulas/sendpedidoreservamarcacao2")
        url = "https://www.myhcgym.com/planoaulas/sendpedidoreservamarcacao2"
        body = {
            "x": "AgF8WWcAzywDwXS1 PIiTb0m5WxQYFILEzeUqMqYsGkvNuMnCqMcz3GhuwDzo Ede470IofeKDypX6vxQdOA3/LF0ch/C39zbuf5CqJOTCuNyFnoL5EPiRtZUKlsOGXoE waaoxthL1WoZCNNzxqno5d TR5l4m2FqsI999pUZ7IR63cTx9mY9HmptffenIyo2S2SlS3u67w8YSk2kQ1Ih2H DvGLNpdF46hywA5vi20CNzqG ONmxMPo6EEXtC796Dalyt3C4ey/r73lysgdzLMa7bop4VVguDfVZbPMIZ3BAiY3UIt0TswFbKvr/5e2xoukuu6heefeRXwZNnmaZbaWh9ehcPaEbyDxGmqFFG4iv7Q02QSrdczZSWURBImnfq/FeagOlnugiv8xpaTmIzSsQGD3nyVXL33RQraPW3mlWT0F7Jb0q9B4Colc5ymKi8="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    print("#########################################################################################")
    print("Action: Access meal plan suggestions.")
    try:
        print("POST request to https://www.gymcompany.com/planoalimentar/downloadPDFnut")
        url = "https://www.myhcgym.com/planoalimentar/downloadPDFnut"
        body = {
            "x": "AgFlIEHjMLH8qWPTsBGuv2MfeoeMX m44cXpqHL1lwzYWRn/YGWe/6Q4vQvU7m jTkK3O BlB3/BhIFv60X7yCgpcVbzpCC5aceV25Jw7RDjmfIi4xYPQfv5ZnzJEkjlLs9e 1mmcMZewoy26MPLi2Wkb/gmvH88ZgKWubyboxFLw51IABIdiVoIxe/m/zcAKvM66mqjArl2GdyGZjybcDVWLafMrogq2oysHGPPc4JUEg=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

    print("#########################################################################################")
    print("Action: Access the training plan.")
    try:
        print("POST request to https://www.gymcompany.com/ppwebservice/showptws")
        url = "https://www.myhcgym.com/ppwebservice/showptws"
        body = {
            "x": "AgGC/UuYqqyu6Wzm9Szk0HxRIj7Mcuey93wHl0rLe2akMhf0c72CeMRbIB5S61ZhavRkspkvMPvQaQIxvNYDnk1cX0ua75OBw8ZTFUpP 5T6JgVT5S/gZTTdGeHWc4y5nVCY7PRQtoispol1R7NdV7hPnZr5CZzgeHzp1Bo2SXLofBXWpv2lLIAgaZYeJa9KkgGCP5Bomh/luPDc0gZrCy UHINm/EoVXoAFbGEC4ZSIQTqkduIdVp1jQZNNakZ5LLOmqLYVa2YHX3 ws0 F/ob5ZLvq8e3PACKWHLfB478Z5Q=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)
    
    print("#########################################################################################")
    print("Action: Access the physical assessment history.")
    try:
        print("POST request to https://www.gymcompany.com/avaliacoes/showaval")
        url = "https://www.myhcgym.com/avaliacoes/showaval"
        body = {
            "x": "AgHn4bo 8kZeKoiRczjLCO7Yx5GSfwdCRmfi/Mw2VjoWTMgorvIIAGldkMCeAM9pBfRVPR0tCwK Ix7CnqqFzJQ03myt/g53rvmbHddyNu J3U7fbPh0cypQCYSjl0F0/6DzitNiiNchP/9JpZnAIzN d5FQgjWpEspBQ9k6HKyJne8RvJ8YcY4lxomr8OW2LNOWd8qYWvnLEm97ZEkbVgeGJv9iXG6VssnHAY6O9UPqIGouuERKcyiJlE7JDYq4vWVB7pCMMpDqqHlMPHii8sGj7H2XVSAUdrWmLB9vbmhCPg=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)
    
    print("#########################################################################################")
    print("Action: Send a question about the physical assessment.")
    try:
        print("POST request to https://www.gymcompany.com/actividade/insertagenda")
        url = "https://www.myhcgym.com/actividade/insertagenda"
        body = {
            "x": "AgEMr1sBB33e ukqMJuNmczp  TSZRhP9eLy597o5MUfgA0IHbXn/FneHdedIYYC30NqL1ooSLRhjSATJ h1SPkjJ0hIu8gCY Ra WCKGKMK3z36m030OD3sfhgXjSm3XCXe6LXK1Wo4YTQWdA XjWGeeLrQn1X7T571i0Z73JHsNrO5FTbWFqR8JIXCiHkJhNAIz18q0GaFw2 1QdaT7kORxkqcitvEO6VxCxYnMIDCBUcs7wgchnGpvN5ZKQVIIMaITIHEKkWrqto k cS OuhvlwJjA5mKzjSSfccZgQChaCi3Jakp0fmPPq6OcHTT0Y79xcg8Iy Gtas/0bSMqczf7Cf3MiIZ3 32ofmHQfGfg=="
        }
        response = requests.post(url, data=body, headers=headers)
        response.raise_for_status()
        print("POST request successful!")
        print("Response content:", response.text)
        print("\n")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)

if __name__ == "__main__":
    main()