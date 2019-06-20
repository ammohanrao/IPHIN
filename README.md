# IPHIN
Indian Public Health Intelligence Network

This is an open source software developed to keep track of disease outbreaks in India. 

We are making our research on ongoing outbreak in Bihar (see https://rubygems.pkg.github.com/ammohanrao/IPHIN/wiki/Is-Acute-Encephalitis-Syndrome-In-Bihar-A-Transmissible-Spongiform-Encephalitis%3F).

Methods: We downloaded PUBMED central publications from its repository and searched xml file using jq.

if grep -wF "Case Report" test.json
	then		
		jq '.article.body.sec[]' test.json >ck1.txt
fi

Clinical data from Case reports is extracted using CTAKES (Clinical Text Analysis and Knowledge Extraction System). 
A JSON file output is processed by jq for extracting disease, feature, procedures along with their SNOMED ID and preferred terms. Processing incudes disambiguation and negation links meaning no item excluded is selected.

The results are given in different files and are described here.

Description of files:
1). enjlist: list of publications which report encephalitis cases.
2). enpjlist: list of publications which report encephalopathy cases.
3). encdfrq: list of "encephalitis like disease" frequency reported in literature.
4). enpfrq: list of "encephalopathy like disease" frequency reported in literature.
5). encffrq: list of "features + procedures" frequency reported in encephalitis diseases in literature.
6). enpffrq: list of "features + procedures" frequency reported in encephalopathy diseases in literature.
7). enp_autopsy: list of publications reporting autopsy and encephalopathy diseases.
8). enc_autopsy: list of publications reporting autopsy and encephalitis diseases.
9). prion_snodis: list of publications reporting prion diseases.

END

Presently it's focus is to search several Indian online news papers including English and other languages like Telugu etc.

This project's aim is to extend the work of GPHIN (Global Public Health Intelligence Network):
https://gphin.canada.ca/cepr/aboutgphin-rmispenbref.jsp?language=en_CA

As GPHIN work is limited to few global languages and does not cover any of Indian languages, we felt the need to fulfill this gap.

We wish to acknowledge our deep sense of respect for Dr.Larry Brilliant whose inspiration we take on this project:
https://www.ted.com/talks/larry_brilliant_wants_to_stop_pandemics?language=en

Instructions:
Hardware: Internet connection.

Software: python3 on linux

Can work on windows.

Download the files and run shell script.

Modify url links to update as necessary.

#IMPORTANT:

Analyse results objectively as output may be misleading. Use discretion for prediction of possible outbreaks as it may spread panic. 
