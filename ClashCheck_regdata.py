import pandas as pd
import sys,os
from collections import defaultdict

course_dict = {'BITS C799T' : 10, 'BITS G561T' : 25, 'BITS G629T' : 10, 'BITS C412' : 20, 'BITS C413' : 20, 'BITS C695T' : 20, 'BITS F412' : 20, 'BITS F413' : 20, 'BITS G560' : 20, 'BITS G639' : 20, 'BITS F421T' : 16, 'BITS F422T' : 16, 'BITS C421T' : 15, 'BITS C422T' : 15, 'BITS F423T' : 9, 'BITS F424T' : 9, 'BITS G529' : 6, 'BITS G539' : 6, 'PHA G642' : 6, 'BENG G521' : 5, 'BIO G510' : 5, 'BIO G512' : 5, 'BIO G513' : 5, 'BIO G514' : 5, 'BIO G523' : 5, 'BIO G524' : 5, 'BIO G525' : 5, 'BIO G526' : 5, 'BIO G542' : 5, 'BIO G544' : 5, 'BIO G545' : 5, 'BIO G611' : 5, 'BIO G612' : 5, 'BIO G632' : 5, 'BIO G642' : 5, 'BIO G643' : 5, 'BIO G651' : 5, 'BIO G671' : 5, 'BITS C221' : 5, 'BITS C231' : 5, 'BITS C241' : 5, 'BITS E661' : 5, 'BITS F221' : 5, 'BITS F231' : 5, 'BITS F241' : 5, 'BITS G511' : 5, 'BITS G513' : 5, 'BITS G553' : 5, 'BITS G554' : 5, 'BITS G612' : 5, 'BITS G613' : 5, 'BITS G624' : 5, 'BITS G641' : 5, 'BITS G644' : 5, 'BITS G649' : 5, 'BITS G654' : 5, 'CE G511' : 5, 'CE G521' : 5, 'CE G522' : 5, 'CE G610' : 5, 'CE G611' : 5, 'CE G619' : 5, 'CE G621' : 5, 'CE G641' : 5, 'CHE G513' : 5, 'CHE G514' : 5, 'CHE G523' : 5, 'CHE G533' : 5, 'CHE G542' : 5, 'CHE G551' : 5, 'CHE G611' : 5, 'CHE G612' : 5, 'CHE G613' : 5, 'CHE G614' : 5, 'CHE G615' : 5, 'CHE G616' : 5, 'CHE G617' : 5, 'CHE G618' : 5, 'CHE G619' : 5, 'CHE G620' : 5, 'CHE G621' : 5, 'CHE G622' : 5, 'CHE G631' : 5, 'CHE G641' : 5, 'CHEM G531' : 5, 'CHEM G541' : 5, 'CHEM G551' : 5, 'CHEM G552' : 5, 'CHEM G553' : 5, 'CHEM G554' : 5, 'CHEM G558' : 5, 'CHEM G561' : 5, 'CS G511' : 5, 'CS G515' : 5, 'CS G523' : 5, 'CS G524' : 5, 'CS G525' : 5, 'CS G526' : 5, 'CS G527' : 5, 'CS G531' : 5, 'CS G551' : 5, 'CS G553' : 5, 'CS G554' : 5, 'CS G562' : 5, 'CS G612' : 5, 'CS G622' : 5, 'CS G623' : 5, 'CS G641' : 5, 'CS G653' : 5, 'CS G671' : 5, 'DE G513' : 5, 'DE G514' : 5, 'DE G522' : 5, 'DE G531' : 5, 'DE G611' : 5, 'DE G631' : 5, 'ECON G531' : 5, 'EEE G510' : 5, 'EEE G520' : 5, 'EEE G521' : 5, 'EEE G522' : 5, 'EEE G531' : 5, 'EEE G541' : 5, 'EEE G542' : 5, 'EEE G544' : 5, 'EEE G552' : 5, 'EEE G559' : 5, 'EEE G581' : 5, 'EEE G582' : 5, 'EEE G591' : 5, 'EEE G592' : 5, 'EEE G612' : 5, 'EEE G613' : 5, 'EEE G621' : 5, 'EEE G622' : 5, 'ENGL G511' : 5, 'ENGL G512' : 5, 'ENGL G521' : 5, 'ENGL G531' : 5, 'ENGL G541' : 5, 'ENGL G611' : 5, 'INSTR G611' : 5, 'INSTR G612' : 5, 'MATH D021' : 5, 'ME G511' : 5, 'ME G512' : 5, 'ME G513' : 5, 'ME G514' : 5, 'ME G515' : 5, 'ME G516' : 5, 'ME G521' : 5, 'ME G532' : 5, 'ME G533' : 5, 'ME G534' : 5, 'ME G535' : 5, 'ME G536' : 5, 'ME G538' : 5, 'ME G539' : 5, 'ME G611' : 5, 'ME G621' : 5, 'ME G631' : 5, 'ME G641' : 5, 'MEL G512' : 5, 'MEL G531' : 5, 'MEL G611' : 5, 'MEL G621' : 5, 'MEL G623' : 5, 'MEL G624' : 5, 'MEL G625' : 5, 'MEL G626' : 5, 'MEL G631' : 5, 'MEL G632' : 5, 'MEL G641' : 5, 'MGTS G511' : 5, 'MGTS G521' : 5, 'MGTS G531' : 5, 'MGTS G561' : 5, 'MPH G510' : 5, 'MPH G661' : 5, 'MSE G511' : 5, 'MSE G513' : 5, 'MSE G521' : 5, 'MSE G531' : 5, 'MST G511' : 5, 'MST G522' : 5, 'MST G531' : 5, 'PHA G510' : 5, 'PHA G511' : 5, 'PHA G532' : 5, 'PHA G541' : 5, 'PHA G542' : 5, 'PHA G543' : 5, 'PHA G544' : 5, 'PHA G611' : 5, 'PHA G612' : 5, 'PHA G613' : 5, 'PHA G614' : 5, 'PHA G615' : 5, 'PHA G616' : 5, 'PHA G617' : 5, 'PHA G618' : 5, 'PHA G619' : 5, 'PHA G621' : 5, 'PHA G622' : 5, 'PHA G632' : 5, 'PHY G511' : 5, 'PHY G521' : 5, 'PHY G531' : 5, 'PHY G541' : 5, 'SS G511' : 5, 'SS G515' : 5, 'SS G516' : 5, 'SS G517' : 5, 'SS G518' : 5, 'SS G523' : 5, 'SS G527' : 5, 'SS G551' : 5, 'SS G554' : 5, 'SS G562' : 5, 'SS G624' : 5, 'SS G641' : 5, 'SS G653' : 5, 'BITS G661' : 3, 'CHE G552' : 3, 'BIO C391' : 4, 'BIO C418' : 4, 'BIO F212' : 4, 'BIO F244' : 4, 'BIO F352' : 4, 'BIO F418' : 4, 'BIO G515' : 4, 'BIO G522' : 4, 'BIO G532' : 4, 'BIO G631' : 4, 'BIO G641' : 4, 'BIO G661' : 4, 'BIOT C337' : 4, 'BIOT C418' : 4, 'BIOT F212' : 4, 'BIOT F241' : 4, 'BIOT F244' : 4, 'BIOT F314' : 4, 'BITS C321' : 4, 'BITS C465' : 4, 'BITS C466' : 4, 'BITS C494' : 4, 'BITS F321' : 4, 'BITS F415' : 4, 'BITS F417' : 4, 'BITS F465' : 4, 'BITS F466' : 4, 'BITS F488' : 4, 'BITS F494' : 4, 'BITS G512' : 4, 'BITS G515' : 4, 'BITS G521' : 4, 'BITS G540' : 4, 'BITS G541' : 4, 'BITS G619' : 4, 'BITS G659' : 4, 'CE C342' : 4, 'CE C361' : 4, 'CE C371' : 4, 'CE C383' : 4, 'CE C391' : 4, 'CE C392' : 4, 'CE C416' : 4, 'CE F213' : 4, 'CE F243' : 4, 'CE F244' : 4, 'CE F311' : 4, 'CE F312' : 4, 'CE F342' : 4, 'CE F416' : 4, 'CE F431' : 4, 'CE F433' : 4, 'CE G512' : 4, 'CE G513' : 4, 'CE G514' : 4, 'CE G515' : 4, 'CE G516' : 4, 'CE G517' : 4, 'CE G518' : 4, 'CE G520' : 4, 'CE G523' : 4, 'CE G524' : 4, 'CE G525' : 4, 'CE G526' : 4, 'CE G527' : 4, 'CE G528' : 4, 'CE G529' : 4, 'CE G530' : 4, 'CE G531' : 4, 'CE G532' : 4, 'CE G533' : 4, 'CE G534' : 4, 'CE G535' : 4, 'CE G536' : 4, 'CE G537' : 4, 'CE G538' : 4, 'CE G539' : 4, 'CE G542' : 4, 'CE G543' : 4, 'CE G545' : 4, 'CE G546' : 4, 'CE G547' : 4, 'CE G548' : 4, 'CE G549' : 4, 'CE G551' : 4, 'CE G552' : 4, 'CE G553' : 4, 'CE G554' : 4, 'CE G612' : 4, 'CE G613' : 4, 'CE G614' : 4, 'CE G615' : 4, 'CE G616' : 4, 'CE G617' : 4, 'CE G618' : 4, 'CE G620' : 4, 'CE G622' : 4, 'CE G623' : 4, 'CE G631' : 4, 'CE G632' : 4, 'CHE C351' : 4, 'CHE C431' : 4, 'CHE C473' : 4, 'CHE G511' : 4, 'CHE G512' : 4, 'CHE G521' : 4, 'CHE G522' : 4, 'CHE G524' : 4, 'CHE G525' : 4, 'CHE G528' : 4, 'CHE G531' : 4, 'CHE G532' : 4, 'CHE G541' : 4, 'CHEM C351' : 4, 'CHEM C391' : 4, 'CHEM F313' : 4, 'CHEM F324' : 4, 'CHEM F329' : 4, 'CHEM F330' : 4, 'CHEM F336' : 4, 'CHEM F341' : 4, 'CHEM G555' : 4, 'CHEM G557' : 4, 'CS C313' : 4, 'CS C321' : 4, 'CS C363' : 4, 'CS C391' : 4, 'CS F111' : 4, 'CS F211' : 4, 'CS F212' : 4, 'CS F213' : 4, 'CS F215' : 4, 'CS F241' : 4, 'CS F303' : 4, 'CS F342' : 4, 'CS F424' : 4, 'CS G513' : 4, 'CS G514' : 4, 'CS G520' : 4, 'CS G521' : 4, 'CS G541' : 4, 'CS G555' : 4, 'CS G611' : 4, 'EA C412' : 4, 'EA C415' : 4, 'EA C417' : 4, 'EA C476' : 4, 'EA C485' : 4, 'ECE C364' : 4, 'ECE C383' : 4, 'ECE C391' : 4, 'ECE F211' : 4, 'ECE F215' : 4, 'ECE F241' : 4, 'ECE F311' : 4, 'ECE F341' : 4, 'ECE F434' : 4, 'EEE C364' : 4, 'EEE C371' : 4, 'EEE C383' : 4, 'EEE C391' : 4, 'EEE C434' : 4, 'EEE F211' : 4, 'EEE F215' : 4, 'EEE F241' : 4, 'EEE F311' : 4, 'EEE F341' : 4, 'EEE F342' : 4, 'EEE F434' : 4, 'EEE G512' : 4, 'EEE G546' : 4, 'EEE G625' : 4, 'EEE G626' : 4, 'EEE G627' : 4, 'ES C263' : 4, 'INSTR C355' : 4, 'INSTR C364' : 4, 'INSTR C371' : 4, 'INSTR C391' : 4, 'INSTR F211' : 4, 'INSTR F215' : 4, 'INSTR F241' : 4, 'INSTR F311' : 4, 'INSTR F341' : 4, 'INSTR F342' : 4, 'INSTR F419' : 4, 'IS C313' : 4, 'IS C351' : 4, 'IS C363' : 4, 'IS F211' : 4, 'IS F213' : 4, 'IS F241' : 4, 'IS F242' : 4, 'IS F243' : 4, 'IS F303' : 4, 'IS F341' : 4, 'ITEB G521' : 4, 'ITEB G522' : 4, 'ITEB G621' : 4, 'MBA C311' : 4, 'MBA C321' : 4, 'MBA C411' : 4, 'MBA C412' : 4, 'MBA C413' : 4, 'MBA C415' : 4, 'MBA C416' : 4, 'MBA C417' : 4, 'MBA C418' : 4, 'MBA C419' : 4, 'MBA C421' : 4, 'MBA C422' : 4, 'MBA C423' : 4, 'MBA C427' : 4, 'MBA C428' : 4, 'MBA C429' : 4, 'MBA C481' : 4, 'MBA G512' : 4, 'MBA G522' : 4, 'MBA G523' : 4, 'MBA G552' : 4, 'MBA G622' : 4, 'ME C331' : 4, 'ME C332' : 4, 'ME C342' : 4, 'ME C411' : 4, 'ME F241' : 4, 'ME F311' : 4, 'ME F313' : 4, 'ME F342' : 4, 'ME F411' : 4, 'ME F423' : 4, 'ME F433' : 4, 'ME G541' : 4, 'MEL G612' : 4, 'MEL G642' : 4, 'MF C314' : 4, 'MF C315' : 4, 'MF C421' : 4, 'MF F241' : 4, 'MF F313' : 4, 'MF F342' : 4, 'MF F343' : 4, 'MF F411' : 4, 'MF F421' : 4, 'MGSYS G521' : 4, 'MGSYS G541' : 4, 'MGSYS G551' : 4, 'MGSYS G611' : 4, 'MGSYS G621' : 4, 'MGSYS G631' : 4, 'MGSYS G641' : 4, 'MM G522' : 4, 'MPH C431' : 4, 'MPH G512' : 4, 'MPH G513' : 4, 'MPH G515' : 4, 'MPH G521' : 4, 'MPH G522' : 4, 'MPH G523' : 4, 'MPH G531' : 4, 'MPH G535' : 4, 'MSE G512' : 4, 'MSE G514' : 4, 'PHA C391' : 4, 'PHA F313' : 4, 'PHA G512' : 4, 'PHA G521' : 4, 'PHA G522' : 4, 'PHA G531' : 4, 'PHA G545' : 4, 'PHA G645' : 4, 'PHY C391' : 4, 'PHY C412' : 4, 'PHY C415' : 4, 'PHY C423' : 4, 'PHY F211' : 4, 'PHY F241' : 4, 'PHY F412' : 4, 'PHY F413' : 4, 'PHY F414' : 4, 'PHY F415' : 4, 'PHY F416' : 4, 'PHY F417' : 4, 'PHY F418' : 4, 'PHY F419' : 4, 'PHY F420' : 4, 'PHY F421' : 4, 'PHY F422' : 4, 'PHY F423' : 4, 'PHY F424' : 4, 'PHY F425' : 4, 'PHY F426' : 4, 'SS G512' : 4, 'SS G513' : 4, 'SS G514' : 4, 'SS G520' : 4, 'SS G521' : 4, 'SS G531' : 4, 'SS G552' : 4, 'TA C111' : 4, 'TA C112' : 4, 'TA C222' : 4, 'BITS F418' : 4, 'CHEM G559' : 3, 'PHY G514' : 3, 'AAOC C111' : 3, 'AAOC C221' : 3, 'AAOC C222' : 3, 'AAOC C311' : 3, 'AAOC C312' : 3, 'AAOC C321' : 3, 'AAOC C341' : 3, 'BIO C111' : 3, 'BIO C211' : 3, 'BIO C231' : 3, 'BIO C241' : 3, 'BIO C312' : 3, 'BIO C321' : 3, 'BIO C322' : 3, 'BIO C331' : 3, 'BIO C332' : 3, 'BIO C341' : 3, 'BIO C342' : 3, 'BIO C352' : 3, 'BIO C411' : 3, 'BIO C412' : 3, 'BIO C413' : 3, 'BIO C414' : 3, 'BIO C416' : 3, 'BIO C417' : 3, 'BIO C419' : 3, 'BIO C421' : 3, 'BIO C431' : 3, 'BIO C441' : 3, 'BIO C451' : 3, 'BIO C461' : 3, 'BIO C491' : 3, 'BIO F111' : 3, 'BIO F211' : 3, 'BIO F213' : 3, 'BIO F214' : 3, 'BIO F215' : 3, 'BIO F231' : 3, 'BIO F241' : 3, 'BIO F242' : 3, 'BIO F243' : 3, 'BIO F266' : 3, 'BIO F311' : 3, 'BIO F312' : 3, 'BIO F313' : 3, 'BIO F341' : 3, 'BIO F342' : 3, 'BIO F366' : 3, 'BIO F367' : 3, 'BIO F376' : 3, 'BIO F377' : 3, 'BIO F411' : 3, 'BIO F413' : 3, 'BIO F417' : 3, 'BIO F419' : 3, 'BIO F421' : 3, 'BIO F431' : 3, 'BIO F441' : 3, 'BIO F451' : 3, 'BIO F491' : 3, 'BIOT C216' : 3, 'BIOT C332' : 3, 'BIOT C336' : 3, 'BIOT C338' : 3, 'BIOT C339' : 3, 'BIOT C343' : 3, 'BIOT C344' : 3, 'BIOT C346' : 3, 'BIOT C416' : 3, 'BIOT C441' : 3, 'BIOT C461' : 3, 'BIOT C463' : 3, 'BIOT C491' : 3, 'BIOT F211' : 3, 'BIOT F213' : 3, 'BIOT F215' : 3, 'BIOT F242' : 3, 'BIOT F243' : 3, 'BIOT F245' : 3, 'BIOT F311' : 3, 'BIOT F342' : 3, 'BIOT F343' : 3, 'BIOT F344' : 3, 'BIOT F345' : 3, 'BIOT F346' : 3, 'BIOT F347' : 3, 'BIOT F352' : 3, 'BIOT F413' : 3, 'BIOT F416' : 3, 'BIOT F417' : 3, 'BIOT F420' : 3, 'BIOT F422' : 3, 'BIOT F423' : 3, 'BIOT F424' : 3, 'BITS C214' : 3, 'BITS C216' : 3, 'BITS C217' : 3, 'BITS C218' : 3, 'BITS C313' : 3, 'BITS C314' : 3, 'BITS C315' : 3, 'BITS C323' : 3, 'BITS C324' : 3, 'BITS C331' : 3, 'BITS C333' : 3, 'BITS C334' : 3, 'BITS C335' : 3, 'BITS C341' : 3, 'BITS C342' : 3, 'BITS C364' : 3, 'BITS C372' : 3, 'BITS C381' : 3, 'BITS C382' : 3, 'BITS C383' : 3, 'BITS C385' : 3, 'BITS C386' : 3, 'BITS C393' : 3, 'BITS C394' : 3, 'BITS C395' : 3, 'BITS C396' : 3, 'BITS C397' : 3, 'BITS C398' : 3, 'BITS C428' : 3, 'BITS C432' : 3, 'BITS C461' : 3, 'BITS C462' : 3, 'BITS C463' : 3, 'BITS C464' : 3, 'BITS C467' : 3, 'BITS C468' : 3, 'BITS C469' : 3, 'BITS C471' : 3, 'BITS C472' : 3, 'BITS C473' : 3, 'BITS C474' : 3, 'BITS C481' : 3, 'BITS C482' : 3, 'BITS C483' : 3, 'BITS C484' : 3, 'BITS C486' : 3, 'BITS C487' : 3, 'BITS C488' : 3, 'BITS C489' : 3, 'BITS C493' : 3, 'BITS F111' : 3, 'BITS F217' : 3, 'BITS F316' : 3, 'BITS F333' : 3, 'BITS F334' : 3, 'BITS F343' : 3, 'BITS F372' : 3, 'BITS F381' : 3, 'BITS F382' : 3, 'BITS F383' : 3, 'BITS F385' : 3, 'BITS F386' : 3, 'BITS F398' : 3, 'BITS F414' : 3, 'BITS F416' : 3, 'BITS F428' : 3, 'BITS F437' : 3, 'BITS F441' : 3, 'BITS F442' : 3, 'BITS F444' : 3, 'BITS F445' : 3, 'BITS F446' : 3, 'BITS F447' : 3, 'BITS F448' : 3, 'BITS F449' : 3, 'BITS F461' : 3, 'BITS F462' : 3, 'BITS F464' : 3, 'BITS F468' : 3, 'BITS F469' : 3, 'BITS F482' : 3, 'BITS F493' : 3, 'BITS G514' : 3, 'BITS G620' : 3, 'BITS G621' : 3, 'CDP C221' : 3, 'CDP C313' : 3, 'CDP C323' : 3, 'CDP C332' : 3, 'CDP C363' : 3, 'CDP C364' : 3, 'CDP C371' : 3, 'CE C212' : 3, 'CE C241' : 3, 'CE C322' : 3, 'CE C381' : 3, 'CE C394' : 3, 'CE C412' : 3, 'CE C414' : 3, 'CE C415' : 3, 'CE C417' : 3, 'CE C418' : 3, 'CE C419' : 3, 'CE C422' : 3, 'CE C432' : 3, 'CE C441' : 3, 'CE C461' : 3, 'CE C471' : 3, 'CE C491' : 3, 'CE F211' : 3, 'CE F212' : 3, 'CE F214' : 3, 'CE F241' : 3, 'CE F242' : 3, 'CE F266' : 3, 'CE F313' : 3, 'CE F323' : 3, 'CE F324' : 3, 'CE F341' : 3, 'CE F343' : 3, 'CE F366' : 3, 'CE F367' : 3, 'CE F376' : 3, 'CE F377' : 3, 'CE F411' : 3, 'CE F412' : 3, 'CE F413' : 3, 'CE F415' : 3, 'CE F417' : 3, 'CE F419' : 3, 'CE F420' : 3, 'CE F421' : 3, 'CE F423' : 3, 'CE F425' : 3, 'CE F426' : 3, 'CE F427' : 3, 'CE F428' : 3, 'CE F429' : 3, 'CE F430' : 3, 'CE F432' : 3, 'CE F434' : 3, 'CE F435' : 3, 'CE F491' : 3, 'CHE C213' : 3, 'CHE C221' : 3, 'CHE C311' : 3, 'CHE C312' : 3, 'CHE C322' : 3, 'CHE C332' : 3, 'CHE C361' : 3, 'CHE C411' : 3, 'CHE C412' : 3, 'CHE C413' : 3, 'CHE C414' : 3, 'CHE C421' : 3, 'CHE C422' : 3, 'CHE C432' : 3, 'CHE C433' : 3, 'CHE C441' : 3, 'CHE C471' : 3, 'CHE C491' : 3, 'CHE F211' : 3, 'CHE F212' : 3, 'CHE F213' : 3, 'CHE F214' : 3, 'CHE F241' : 3, 'CHE F242' : 3, 'CHE F243' : 3, 'CHE F244' : 3, 'CHE F266' : 3, 'CHE F311' : 3, 'CHE F312' : 3, 'CHE F313' : 3, 'CHE F314' : 3, 'CHE F341' : 3, 'CHE F342' : 3, 'CHE F343' : 3, 'CHE F366' : 3, 'CHE F367' : 3, 'CHE F376' : 3, 'CHE F377' : 3, 'CHE F411' : 3, 'CHE F412' : 3, 'CHE F413' : 3, 'CHE F414' : 3, 'CHE F415' : 3, 'CHE F416' : 3, 'CHE F417' : 3, 'CHE F418' : 3, 'CHE F419' : 3, 'CHE F421' : 3, 'CHE F433' : 3, 'CHE F471' : 3, 'CHE F491' : 3, 'CHEM C141' : 3, 'CHEM C142' : 3, 'CHEM C211' : 3, 'CHEM C212' : 3, 'CHEM C221' : 3, 'CHEM C222' : 3, 'CHEM C231' : 3, 'CHEM C232' : 3, 'CHEM C311' : 3, 'CHEM C312' : 3, 'CHEM C321' : 3, 'CHEM C322' : 3, 'CHEM C331' : 3, 'CHEM C332' : 3, 'CHEM C341' : 3, 'CHEM C342' : 3, 'CHEM C352' : 3, 'CHEM C361' : 3, 'CHEM C362' : 3, 'CHEM C411' : 3, 'CHEM C412' : 3, 'CHEM C421' : 3, 'CHEM C422' : 3, 'CHEM C431' : 3, 'CHEM C441' : 3, 'CHEM C451' : 3, 'CHEM C461' : 3, 'CHEM C491' : 3, 'CHEM F111' : 3, 'CHEM F211' : 3, 'CHEM F212' : 3, 'CHEM F213' : 3, 'CHEM F214' : 3, 'CHEM F223' : 3, 'CHEM F241' : 3, 'CHEM F242' : 3, 'CHEM F243' : 3, 'CHEM F244' : 3, 'CHEM F266' : 3, 'CHEM F311' : 3, 'CHEM F312' : 3, 'CHEM F323' : 3, 'CHEM F325' : 3, 'CHEM F326' : 3, 'CHEM F327' : 3, 'CHEM F328' : 3, 'CHEM F333' : 3, 'CHEM F334' : 3, 'CHEM F335' : 3, 'CHEM F337' : 3, 'CHEM F342' : 3, 'CHEM F343' : 3, 'CHEM F366' : 3, 'CHEM F367' : 3, 'CHEM F376' : 3, 'CHEM F377' : 3, 'CHEM F412' : 3, 'CHEM F414' : 3, 'CHEM F415' : 3, 'CHEM F422' : 3, 'CHEM F491' : 3, 'CHI N101T' : 3, 'CS C311' : 3, 'CS C314' : 3, 'CS C332' : 3, 'CS C341' : 3, 'CS C342' : 3, 'CS C351' : 3, 'CS C352' : 3, 'CS C362' : 3, 'CS C372' : 3, 'CS C414' : 3, 'CS C415' : 3, 'CS C422' : 3, 'CS C424' : 3, 'CS C441' : 3, 'CS C442' : 3, 'CS C444' : 3, 'CS C446' : 3, 'CS C451' : 3, 'CS C453' : 3, 'CS C461' : 3, 'CS C471' : 3, 'CS C481' : 3, 'CS C491' : 3, 'CS F214' : 3, 'CS F222' : 3, 'CS F266' : 3, 'CS F314' : 3, 'CS F351' : 3, 'CS F363' : 3, 'CS F364' : 3, 'CS F366' : 3, 'CS F367' : 3, 'CS F372' : 3, 'CS F376' : 3, 'CS F377' : 3, 'CS F401' : 3, 'CS F407' : 3, 'CS F413' : 3, 'CS F415' : 3, 'CS F422' : 3, 'CS F441' : 3, 'CS F446' : 3, 'CS F491' : 3, 'EA C342' : 3, 'EA C411' : 3, 'EA C414' : 3, 'EA C416' : 3, 'EA C422' : 3, 'EA C441' : 3, 'EA C442' : 3, 'EA C443' : 3, 'EA C451' : 3, 'EA C452' : 3, 'EA C461' : 3, 'EA C462' : 3, 'EA C463' : 3, 'EA C471' : 3, 'EA C472' : 3, 'EA C473' : 3, 'EA C474' : 3, 'EA C475' : 3, 'EA C481' : 3, 'EA C482' : 3, 'ECE C272' : 3, 'ECE C313' : 3, 'ECE C392' : 3, 'ECE C393' : 3, 'ECE C394' : 3, 'ECE C452' : 3, 'ECE C491' : 3, 'ECE F212' : 3, 'ECE F214' : 3, 'ECE F242' : 3, 'ECE F243' : 3, 'ECE F244' : 3, 'ECE F266' : 3, 'ECE F314' : 3, 'ECE F344' : 3, 'ECE F366' : 3, 'ECE F367' : 3, 'ECE F376' : 3, 'ECE F377' : 3, 'ECE F414' : 3, 'ECE F416' : 3, 'ECE F418' : 3, 'ECE F431' : 3, 'ECE F472' : 3, 'ECE F491' : 3, 'ECON C211' : 3, 'ECON C212' : 3, 'ECON C311' : 3, 'ECON C321' : 3, 'ECON C322' : 3, 'ECON C341' : 3, 'ECON C342' : 3, 'ECON C362' : 3, 'ECON C372' : 3, 'ECON C411' : 3, 'ECON C412' : 3, 'ECON C421' : 3, 'ECON C422' : 3, 'ECON C431' : 3, 'ECON C436' : 3, 'ECON C451' : 3, 'ECON C461' : 3, 'ECON C471' : 3, 'ECON C481' : 3, 'ECON C491' : 3, 'ECON F211' : 3, 'ECON F212' : 3, 'ECON F213' : 3, 'ECON F214' : 3, 'ECON F241' : 3, 'ECON F242' : 3, 'ECON F243' : 3, 'ECON F244' : 3, 'ECON F266' : 3, 'ECON F311' : 3, 'ECON F312' : 3, 'ECON F313' : 3, 'ECON F314' : 3, 'ECON F341' : 3, 'ECON F342' : 3, 'ECON F343' : 3, 'ECON F351' : 3, 'ECON F352' : 3, 'ECON F353' : 3, 'ECON F354' : 3, 'ECON F355' : 3, 'ECON F356' : 3, 'ECON F357' : 3, 'ECON F366' : 3, 'ECON F367' : 3, 'ECON F376' : 3, 'ECON F377' : 3, 'ECON F411' : 3, 'ECON F412' : 3, 'ECON F413' : 3, 'ECON F414' : 3, 'ECON F415' : 3, 'ECON F422' : 3, 'ECON F471' : 3, 'ECON F491' : 3, 'EEE C272' : 3, 'EEE C374' : 3, 'EEE C381' : 3, 'EEE C382' : 3, 'EEE C414' : 3, 'EEE C415' : 3, 'EEE C416' : 3, 'EEE C417' : 3, 'EEE C422' : 3, 'EEE C424' : 3, 'EEE C432' : 3, 'EEE C433' : 3, 'EEE C441' : 3, 'EEE C443' : 3, 'EEE C444' : 3, 'EEE C452' : 3, 'EEE C453' : 3, 'EEE C461' : 3, 'EEE C462' : 3, 'EEE C471' : 3, 'EEE C472' : 3, 'EEE C491' : 3, 'EEE F111' : 3, 'EEE F212' : 3, 'EEE F214' : 3, 'EEE F242' : 3, 'EEE F243' : 3, 'EEE F244' : 3, 'EEE F266' : 3, 'EEE F312' : 3, 'EEE F313' : 3, 'EEE F345' : 3, 'EEE F366' : 3, 'EEE F367' : 3, 'EEE F376' : 3, 'EEE F377' : 3, 'EEE F414' : 3, 'EEE F416' : 3, 'EEE F418' : 3, 'EEE F422' : 3, 'EEE F425' : 3, 'EEE F426' : 3, 'EEE F427' : 3, 'EEE F431' : 3, 'EEE F432' : 3, 'EEE F433' : 3, 'EEE F435' : 3, 'EEE F472' : 3, 'EEE F491' : 3, 'EEE G543' : 3, 'EEE G545' : 3, 'EEE G553' : 3, 'EEE G554' : 3, 'EEE G555' : 3, 'EEE G556' : 3, 'EEE G557' : 3, 'ENGG C111' : 3, 'ENGG C212' : 3, 'ENGG C232' : 3, 'ENGG C241' : 3, 'ENGG C242' : 3, 'ENGG C264' : 3, 'ENGG C272' : 3, 'ENGG C282' : 3, 'ENGG C291' : 3, 'ENGL C121' : 3, 'ENGL C122' : 3, 'ENGL C123' : 3, 'ENGL C251' : 3, 'ENGL C252' : 3, 'ENGL C261' : 3, 'ENGL C262' : 3, 'ENGL C312' : 3, 'ENGL C321' : 3, 'ENGL C331' : 3, 'ENGL C341' : 3, 'ENGL C342' : 3, 'ENGL C353' : 3, 'ENGL C361' : 3, 'ENGL C362' : 3, 'ENGL C371' : 3, 'ENGL C372' : 3, 'ENGL C441' : 3, 'ENGL C452' : 3, 'ENGL C461' : 3, 'ENGL C491' : 3, 'ES C112' : 3, 'ES C221' : 3, 'ES C222' : 3, 'ES C231' : 3, 'ES C232' : 3, 'ES C233' : 3, 'ES C241' : 3, 'ES C242' : 3, 'ES C252' : 3, 'ES C261' : 3, 'ES C262' : 3, 'ES C272' : 3, 'ET C311' : 3, 'ET C312' : 3, 'ET C322' : 3, 'ET C331' : 3, 'ET C332' : 3, 'ET C341' : 3, 'ET C342' : 3, 'ET C351' : 3, 'ET C352' : 3, 'ET C362' : 3, 'ET C412' : 3, 'ET C413' : 3, 'ET C414' : 3, 'ET C422' : 3, 'ET C432' : 3, 'ET C441' : 3, 'ET C491' : 3, 'FIN C311' : 3, 'FIN C312' : 3, 'FIN C321' : 3, 'FIN C322' : 3, 'FIN C331' : 3, 'FIN C332' : 3, 'FIN C341' : 3, 'FIN C342' : 3, 'FIN C411' : 3, 'FIN C413' : 3, 'FIN C422' : 3, 'FIN C424' : 3, 'FIN C431' : 3, 'FIN C432' : 3, 'FIN C433' : 3, 'FIN C436' : 3, 'FIN C441' : 3, 'FIN C442' : 3, 'FIN C451' : 3, 'FIN C462' : 3, 'FIN C491' : 3, 'FIN F212' : 3, 'FIN F213' : 3, 'FIN F214' : 3, 'FIN F242' : 3, 'FIN F243' : 3, 'FIN F244' : 3, 'FIN F266' : 3, 'FIN F311' : 3, 'FIN F312' : 3, 'FIN F313' : 3, 'FIN F314' : 3, 'FIN F315' : 3, 'FIN F341' : 3, 'FIN F342' : 3, 'FIN F366' : 3, 'FIN F367' : 3, 'FIN F376' : 3, 'FIN F377' : 3, 'FIN F491' : 3, 'FRE N101T' : 3, 'GER N101T' : 3, 'GER N102T' : 3, 'GS F211' : 3, 'GS F212' : 3, 'GS F213' : 3, 'GS F221' : 3, 'GS F222' : 3, 'GS F223' : 3, 'GS F224' : 3, 'GS F231' : 3, 'GS F232' : 3, 'GS F233' : 3, 'GS F234' : 3, 'GS F241' : 3, 'GS F242' : 3, 'GS F243' : 3, 'GS F244' : 3, 'GS F245' : 3, 'GS F266' : 3, 'GS F311' : 3, 'GS F312' : 3, 'GS F321' : 3, 'GS F322' : 3, 'GS F325' : 3, 'GS F326' : 3, 'GS F327' : 3, 'GS F331' : 3, 'GS F332' : 3, 'GS F333' : 3, 'GS F334' : 3, 'GS F341' : 3, 'GS F342' : 3, 'GS F343' : 3, 'GS F366' : 3, 'GS F367' : 3, 'GS F376' : 3, 'GS F377' : 3, 'GS F491' : 3, 'HIST C112' : 3, 'HIST C211' : 3, 'HIST C213' : 3, 'HSS C221' : 3, 'HSS C222' : 3, 'HSS C231' : 3, 'HSS C232' : 3, 'HSS C241' : 3, 'HSS C313' : 3, 'HSS C314' : 3, 'HSS C316' : 3, 'HSS C317' : 3, 'HSS C318' : 3, 'HSS F222' : 3, 'HSS F223' : 3, 'HSS F226' : 3, 'HSS F227' : 3, 'HSS F228' : 3, 'HSS F232' : 3, 'HSS F233' : 3, 'HSS F234' : 3, 'HSS F235' : 3, 'HSS F236' : 3, 'HSS F266' : 3, 'HSS F316' : 3, 'HSS F317' : 3, 'HSS F318' : 3, 'HSS F323' : 3, 'HSS F325' : 3, 'HSS F326' : 3, 'HSS F327' : 3, 'HSS F328' : 3, 'HSS F329' : 3, 'HSS F332' : 3, 'HSS F333' : 3, 'HSS F334' : 3, 'HSS F338' : 3, 'HSS F339' : 3, 'HSS F343' : 3, 'HSS F344' : 3, 'HSS F345' : 3, 'HSS F346' : 3, 'HUM C121' : 3, 'HUM C232' : 3, 'HUM C311' : 3, 'HUM C312' : 3, 'HUM C321' : 3, 'HUM C331' : 3, 'HUM C332' : 3, 'HUM C341' : 3, 'HUM C342' : 3, 'HUM C351' : 3, 'HUM C352' : 3, 'HUM C371' : 3, 'HUM C372' : 3, 'HUM C381' : 3, 'HUM C382' : 3, 'HUM C383' : 3, 'HUM C411' : 3, 'HUM C412' : 3, 'HUM C413' : 3, 'HUM C421' : 3, 'HUM C431' : 3, 'HUM G511' : 3, 'INSTR C272' : 3, 'INSTR C312' : 3, 'INSTR C313' : 3, 'INSTR C354' : 3, 'INSTR C381' : 3, 'INSTR C392' : 3, 'INSTR C411' : 3, 'INSTR C414' : 3, 'INSTR C421' : 3, 'INSTR C444' : 3, 'INSTR C451' : 3, 'INSTR C461' : 3, 'INSTR C471' : 3, 'INSTR C481' : 3, 'INSTR C491' : 3, 'INSTR F212' : 3, 'INSTR F214' : 3, 'INSTR F242' : 3, 'INSTR F243' : 3, 'INSTR F244' : 3, 'INSTR F266' : 3, 'INSTR F312' : 3, 'INSTR F313' : 3, 'INSTR F343' : 3, 'INSTR F366' : 3, 'INSTR F367' : 3, 'INSTR F376' : 3, 'INSTR F377' : 3, 'INSTR F412' : 3, 'INSTR F413' : 3, 'INSTR F414' : 3, 'INSTR F415' : 3, 'INSTR F420' : 3, 'INSTR F422' : 3, 'INSTR F432' : 3, 'INSTR F491' : 3, 'IS C311' : 3, 'IS C312' : 3, 'IS C314' : 3, 'IS C321' : 3, 'IS C331' : 3, 'IS C332' : 3, 'IS C341' : 3, 'IS C342' : 3, 'IS C352' : 3, 'IS C361' : 3, 'IS C362' : 3, 'IS C411' : 3, 'IS C415' : 3, 'IS C421' : 3, 'IS C422' : 3, 'IS C424' : 3, 'IS C431' : 3, 'IS C442' : 3, 'IS C444' : 3, 'IS C446' : 3, 'IS C461' : 3, 'IS C462' : 3, 'IS C471' : 3, 'IS C472' : 3, 'IS C481' : 3, 'IS F214' : 3, 'IS F222' : 3, 'IS F266' : 3, 'IS F311' : 3, 'IS F322' : 3, 'IS F342' : 3, 'IS F366' : 3, 'IS F367' : 3, 'IS F372' : 3, 'IS F376' : 3, 'IS F377' : 3, 'IS F462' : 3, 'IS F491' : 3, 'JAP N101T' : 3, 'MATH C121' : 3, 'MATH C131' : 3, 'MATH C191' : 3, 'MATH C192' : 3, 'MATH C222' : 3, 'MATH C231' : 3, 'MATH C241' : 3, 'MATH C311' : 3, 'MATH C312' : 3, 'MATH C321' : 3, 'MATH C322' : 3, 'MATH C331' : 3, 'MATH C332' : 3, 'MATH C352' : 3, 'MATH C353' : 3, 'MATH C411' : 3, 'MATH C412' : 3, 'MATH C421' : 3, 'MATH C431' : 3, 'MATH C441' : 3, 'MATH C451' : 3, 'MATH C452' : 3, 'MATH C481' : 3, 'MATH C491' : 3, 'MATH F111' : 3, 'MATH F112' : 3, 'MATH F113' : 3, 'MATH F211' : 3, 'MATH F212' : 3, 'MATH F213' : 3, 'MATH F214' : 3, 'MATH F215' : 3, 'MATH F231' : 3, 'MATH F241' : 3, 'MATH F242' : 3, 'MATH F243' : 3, 'MATH F244' : 3, 'MATH F266' : 3, 'MATH F311' : 3, 'MATH F312' : 3, 'MATH F313' : 3, 'MATH F314' : 3, 'MATH F341' : 3, 'MATH F342' : 3, 'MATH F343' : 3, 'MATH F353' : 3, 'MATH F354' : 3, 'MATH F366' : 3, 'MATH F367' : 3, 'MATH F376' : 3, 'MATH F377' : 3, 'MATH F421' : 3, 'MATH F431' : 3, 'MATH F441' : 3, 'MATH F471' : 3, 'MATH F481' : 3, 'MATH F491' : 3, 'MBA C312' : 3, 'MBA C313' : 3, 'MBA C314' : 3, 'MBA C315' : 3, 'MBA C323' : 3, 'MBA C341' : 3, 'MBA C414' : 3, 'MBA C424' : 3, 'MBA C425' : 3, 'MBA C432' : 3, 'MBA C433' : 3, 'MBA C436' : 3, 'MBA C437' : 3, 'MBA C442' : 3, 'MBA C451' : 3, 'MBA C454' : 3, 'MBA C462' : 3, 'MBA C463' : 3, 'MBA C471' : 3, 'MBA C474' : 3, 'MBA C475' : 3, 'MBA C482' : 3, 'MBA C483' : 3, 'MBA C486' : 3, 'MBA C488' : 3, 'MBA C489' : 3, 'MBA C493' : 3, 'ME C211' : 3, 'ME C212' : 3, 'ME C312' : 3, 'ME C314' : 3, 'ME C382' : 3, 'ME C392' : 3, 'ME C412' : 3, 'ME C422' : 3, 'ME C432' : 3, 'ME C441' : 3, 'ME C442' : 3, 'ME C443' : 3, 'ME C451' : 3, 'ME C452' : 3, 'ME C461' : 3, 'ME C472' : 3, 'ME C481' : 3, 'ME C491' : 3, 'ME F211' : 3, 'ME F212' : 3, 'ME F214' : 3, 'ME F243' : 3, 'ME F244' : 3, 'ME F266' : 3, 'ME F312' : 3, 'ME F341' : 3, 'ME F343' : 3, 'ME F366' : 3, 'ME F367' : 3, 'ME F376' : 3, 'ME F377' : 3, 'ME F412' : 3, 'ME F413' : 3, 'ME F415' : 3, 'ME F416' : 3, 'ME F417' : 3, 'ME F418' : 3, 'ME F419' : 3, 'ME F420' : 3, 'ME F432' : 3, 'ME F441' : 3, 'ME F443' : 3, 'ME F451' : 3, 'ME F452' : 3, 'ME F461' : 3, 'ME F472' : 3, 'ME F481' : 3, 'ME F491' : 3, 'MF C211' : 3, 'MF C212' : 3, 'MF C312' : 3, 'MF C313' : 3, 'MF C316' : 3, 'MF C319' : 3, 'MF C321' : 3, 'MF C382' : 3, 'MF C411' : 3, 'MF C414' : 3, 'MF C418' : 3, 'MF C441' : 3, 'MF C491' : 3, 'MF F211' : 3, 'MF F212' : 3, 'MF F214' : 3, 'MF F243' : 3, 'MF F244' : 3, 'MF F266' : 3, 'MF F311' : 3, 'MF F312' : 3, 'MF F341' : 3, 'MF F366' : 3, 'MF F367' : 3, 'MF F376' : 3, 'MF F377' : 3, 'MF F412' : 3, 'MF F413' : 3, 'MF F414' : 3, 'MF F418' : 3, 'MF F442' : 3, 'MF F453' : 3, 'MF F463' : 3, 'MF F471' : 3, 'MF F472' : 3, 'MF F473' : 3, 'MF F474' : 3, 'MF F491' : 3, 'MGTS C211' : 3, 'MGTS C233' : 3, 'MGTS C322' : 3, 'MGTS C351' : 3, 'MGTS C362' : 3, 'MGTS C371' : 3, 'MGTS C372' : 3, 'MGTS C381' : 3, 'MGTS C382' : 3, 'MGTS C392' : 3, 'MGTS C412' : 3, 'MGTS C414' : 3, 'MGTS C422' : 3, 'MGTS C424' : 3, 'MGTS C432' : 3, 'MGTS C433' : 3, 'MGTS C441' : 3, 'MGTS C442' : 3, 'MGTS C443' : 3, 'MGTS C451' : 3, 'MGTS C452' : 3, 'MGTS C453' : 3, 'MGTS C461' : 3, 'MGTS C462' : 3, 'MGTS C463' : 3, 'MGTS C472' : 3, 'MGTS C473' : 3, 'MGTS C481' : 3, 'MGTS C482' : 3, 'MGTS C483' : 3, 'MGTS C491' : 3, 'MGTS F211' : 3, 'MPH G537' : 3, 'MPH G538' : 3, 'MPH G539' : 3, 'MPH G540' : 3, 'MPH G665' : 3, 'MPH G681' : 3, 'MUSIC N103T' : 3, 'MUSIC N104T' : 3, 'MUSIC N105T' : 3, 'MUSIC N111T' : 3, 'MUSIC N112T' : 3, 'MUSIC N113T' : 3, 'MUSIC N114T' : 3, 'MUSIC N203T' : 3, 'MUSIC N204T' : 3, 'MUSIC N213T' : 3, 'PHA C211' : 3, 'PHA C212' : 3, 'PHA C213' : 3, 'PHA C241' : 3, 'PHA C311' : 3, 'PHA C312' : 3, 'PHA C321' : 3, 'PHA C322' : 3, 'PHA C331' : 3, 'PHA C332' : 3, 'PHA C342' : 3, 'PHA C411' : 3, 'PHA C413' : 3, 'PHA C414' : 3, 'PHA C415' : 3, 'PHA C416' : 3, 'PHA C417' : 3, 'PHA C421' : 3, 'PHA C422' : 3, 'PHA C431' : 3, 'PHA C441' : 3, 'PHA C442' : 3, 'PHA C461' : 3, 'PHA C491' : 3, 'PHA F211' : 3, 'PHA F212' : 3, 'PHA F213' : 3, 'PHA F214' : 3, 'PHA F241' : 3, 'PHA F242' : 3, 'PHA F243' : 3, 'PHA F244' : 3, 'PHA F266' : 3, 'PHA F311' : 3, 'PHA F312' : 3, 'PHA F314' : 3, 'PHA F341' : 3, 'PHA F342' : 3, 'PHA F344' : 3, 'PHA F366' : 3, 'PHA F367' : 3, 'PHA F376' : 3, 'PHA F377' : 3, 'PHA F413' : 3, 'PHA F414' : 3, 'PHA F415' : 3, 'PHA F416' : 3, 'PHA F417' : 3, 'PHA F422' : 3, 'PHA F432' : 3, 'PHA F441' : 3, 'PHA F442' : 3, 'PHA F461' : 3, 'PHA F491' : 3, 'PHIL C211' : 3, 'PHIL C221' : 3, 'PHY C122' : 3, 'PHY C131' : 3, 'PHY C132' : 3, 'PHY C212' : 3, 'PHY C221' : 3, 'PHY C231' : 3, 'PHY C232' : 3, 'PHY C242' : 3, 'PHY C311' : 3, 'PHY C312' : 3, 'PHY C321' : 3, 'PHY C322' : 3, 'PHY C332' : 3, 'PHY C341' : 3, 'PHY C351' : 3, 'PHY C352' : 3, 'PHY C353' : 3, 'PHY C362' : 3, 'PHY C411' : 3, 'PHY C421' : 3, 'PHY C422' : 3, 'PHY C432' : 3, 'PHY C451' : 3, 'PHY C461' : 3, 'PHY C471' : 3, 'PHY C491' : 3, 'PHY F111' : 3, 'PHY F212' : 3, 'PHY F213' : 3, 'PHY F215' : 3, 'PHY F242' : 3, 'PHY F243' : 3, 'PHY F266' : 3, 'PHY F311' : 3, 'PHY F312' : 3, 'PHY F313' : 3, 'PHY F315' : 3, 'PHY F341' : 3, 'PHY F342' : 3, 'PHY F343' : 3, 'PHY F344' : 3, 'PHY F366' : 3, 'PHY F367' : 3, 'PHY F376' : 3, 'PHY F377' : 3, 'PHY F427' : 3, 'PHY F491' : 3, 'POL C211' : 3, 'POL C212' : 3, 'POL C311' : 3, 'POL C312' : 3, 'POL C321' : 3, 'PSY C211' : 3, 'PSY C311' : 3, 'RUS N101T' : 3, 'RUS N102T' : 3, 'SANS C111' : 3, 'SOC C211' : 3, 'SS G542' : 3, 'STD C422' : 3, 'STD C452' : 3, 'STD C491' : 3, 'TA C162' : 3, 'TA C231' : 3, 'TA C252' : 3, 'TA C311' : 3, 'TA C312' : 3, 'TOC C212' : 3, 'TOC C213' : 3, 'TOC C215' : 3, 'TOC C223' : 3, 'TOC C224' : 3, 'TOC C235' : 3, 'TOC C236' : 3, 'TOC C244' : 3, 'TOC C253' : 3, 'BITS F431' : 3, 'BITS F312' : 3, 'BITS F463' : 3, 'CS F469' : 3, 'HSS F221' : 3, 'HSS F336' : 3, 'HSS F337' : 3, 'HSS F347' : 3, 'HSS F349' : 3, 'BIO F314' : 3, 'BITS F419' : 3, 'HSS F340' : 3, 'HSS F341' : 3, 'HSS F342' : 3, 'HSS F350' : 3, 'SANS F111' : 3, 'EEE F473' : 3, 'INSTR F473' : 3, 'MATH F456' : 3, 'ME F485' : 3, 'ECON F315' : 3, 'ECON F435' : 3, 'HSS F355' : 3, 'HSS F356' : 3, 'HSS F399' : 3, 'HSS FN202T' : 3, 'MATH F422' : 3, 'MATH F424' : 3, 'MGTS F433' : 3, 'BITS F317' : 3, 'ECON F434' : 3, 'HSS F229' : 3, 'HSS F335' : 3, 'MATH F444' : 3, 'PHY F345' : 3, 'FIN F414' : 3, 'HSS F314' : 3, 'HSS F353' : 3, 'CHE F422' : 3, 'MATH F423' : 3, 'BIO F217' : 3, 'BIO F216' : 3, 'BIOT C345' : 3, 'BIOT C413' : 3, 'BIOT C414' : 3, 'BIOT C417' : 3, 'BIOT F266' : 3, 'BIOT F366' : 3, 'BIOT F367' : 3, 'BIOT F376' : 3, 'BIOT F377' : 3, 'BIOT F491' : 3, 'BITS C212' : 3, 'BITS C419' : 3, 'BITS C485' : 3, 'BITS E573' : 3, 'BITS E662' : 3, 'BITS F212' : 3, 'BITS F311' : 3, 'BITS F313' : 3, 'BITS F345' : 3, 'BITS F364' : 3, 'BITS F442T' : 3, 'BITS F467' : 3, 'BITS G640' : 3, 'CDP C211' : 3, 'CE G519' : 3, 'CE G555' : 3, 'CE G556' : 3, 'CE G557' : 3, 'CE G558' : 3, 'CE G559' : 3, 'CE G560' : 3, 'CE G561' : 3, 'CHE G526' : 3, 'CHE G527' : 3, 'CHE G529' : 3, 'CHEM F413' : 3, 'CHEM G513' : 3, 'CHEM G521' : 3, 'CHEM G556' : 3, 'CHEM G562' : 3, 'CHEM G563' : 3, 'CS G512' : 3, 'CS G631' : 3, 'CS G632' : 3, 'CS G642' : 3, 'CS G651' : 3, 'CS G652' : 3, 'DE G521' : 3, 'ECE F315' : 3, 'ECE F343' : 3, 'ECON F416' : 3, 'EEE C418' : 3, 'EEE C423' : 3, 'EEE G558' : 3, 'EEE G611' : 3, 'ENGL C222' : 3, 'ET C421' : 3, 'ET C431' : 3, 'FIN C421' : 3, 'FRE N102T' : 3, 'HIST F211' : 3, 'HSS F312' : 3, 'HSS F315' : 3, 'HSS F331' : 3, 'HSS F348' : 3, 'HUM C233' : 3, 'INSTR F411' : 3, 'ITEB G552' : 3, 'MATH C461' : 3, 'MATH C471' : 3, 'MATH G521' : 3, 'MATH G531' : 3, 'MATH G541' : 3, 'MBA C426' : 3, 'ME G537' : 3, 'MEL G622' : 3, 'MF C318' : 3, 'MF C343' : 3, 'MF C412' : 3, 'MF C413' : 3, 'MF C415' : 3, 'MF C416' : 3, 'MF C417' : 3, 'MF C432' : 3, 'MF C442' : 3, 'MF C453' : 3, 'MF C472' : 3, 'MF C473' : 3, 'MF C474' : 3, 'MF C481' : 3, 'MUSIC N106T' : 3, 'MUSIC N205T' : 3, 'MUSIC N206T' : 3, 'MUSIC N214T' : 3, 'MUSIC N303T' : 3, 'MUSIC N313T' : 3, 'PHA C412' : 3, 'PHA C432' : 3, 'PHIL F211' : 3, 'PHIL F221' : 3, 'PHY G513' : 3, 'PHY G515' : 3, 'PHY G516' : 3, 'PHY G517' : 3, 'POL F311' : 3, 'POL F321' : 3, 'SS G522' : 3, 'SS G532' : 3, 'SS G541' : 3, 'BIO G561' : 3, 'HSS N201T' : 2, 'BITS C215' : 2, 'BITS C319' : 2, 'BITS C320' : 2, 'BITS C790T' : 2, 'BITS C797T' : 2, 'BITS F110' : 2, 'BITS F112' : 2, 'BITS F215' : 2, 'BITS F319' : 2, 'BITS F320' : 2, 'CHEM C121' : 2, 'CHEM C122' : 2, 'CHEM C131' : 2, 'CS F301' : 2, 'EEE F346' : 2, 'HSS C319' : 2, 'HSS F319' : 2, 'IS F301' : 2, 'MBA C319' : 2, 'MBA C320' : 2, 'MBA C322' : 2, 'MBA C431' : 2, 'ME F110' : 2, 'ME F213' : 2, 'ME F215' : 2, 'ME F242' : 2, 'ME F344' : 2, 'MF F213' : 2, 'MF F215' : 2, 'MF F242' : 2, 'MF F344' : 2, 'MPH G613' : 2, 'MPH G692' : 2, 'PHA F343' : 2, 'PHY F214' : 2, 'PHY F244' : 2, 'TA C152' : 2, 'TA C211' : 2, 'BIO F110' : 1, 'BITS C211' : 1, 'BITS C213' : 1, 'BITS C317' : 1, 'BITS C318' : 1, 'BITS C441T' : 1, 'BITS C442T' : 1, 'BITS C452T' : 1, 'BITS C791T' : 1, 'BITS C792T' : 1, 'BITS E793T' : 1, 'BITS E794T' : 1, 'BITS F211' : 1, 'BITS F213' : 1, 'BITS F441T' : 1, 'BITS N101T' : 1, 'CHEM F110' : 1, 'HSS C212' : 1, 'HSS F212' : 1, 'MBA C317' : 1, 'PHY F110' : 1,'ME F483' : 3,'HSS F369' : 3,'HSS G512' : 5,'ECON G541' : 5,'SAN G513' : 5,'PHY F428' : 3,'BITS F225' : 3,'MATH F420' : 4,'BITS G518' : 5,'SAN G511' : 5,'ME F424' :	3,'SAN G512' : 5,'BITS G562T' :	16,'BITS F314' : 3,'ECON F345' : 3,'HSS F363' :	3,'HSS G511' :	5,'BITS F315' :	3,'HSS F237' : 3}
course_not_found = set()
class timing:
    def __init__(self,day,start,end):
        self.day=day
        self.start=start
        self.end=end

    def __str__(self):
        return self.day+" "+str(self.start)+" "+str(self.end)

class student:
    def __init__(self,Id,name):
        self.Id=Id
        self.name=name
        self.courseslist=[]
        self.classtimings=[]
        self.compretimings=[]
        self.max_units = self.get_max_unit()
        self.cur_units=0
    def get_max_unit(self):
        if self.Id[4] in "AB":return 25
        elif self.Id[4] in "P":return 100
        else: return 20

    def add_course(self,subject):
        self.courseslist.append(subject)

    def generate_class_timings(self):
        self.classtimings=[]
        for i in self.courseslist:
            if i in classtimes:self.classtimings.append([i,classtimes[i]])

    def generate_compre_dates(self):
        self.compretimings=[]
        for i in self.courseslist:
            if int(i[0]) in compredates:
                if (int(i[0]),compredates[int(i[0])]) not in self.compretimings:self.compretimings.append((int(i[0]),compredates[int(i[0])]))
    
    def authenticate_compre_dates(self):
        global compre_conflict
        global subject_code_to_courseid
        temp_dict={}
        for course_id,compre_time in self.compretimings:
            if (compre_time[0],compre_time[1]) in temp_dict :
                compre_conflict.append(["COMPRE_CONFLICT",self.Id,self.name,min(subject_code_to_courseid[int(temp_dict[(compre_time[0],compre_time[1])])],subject_code_to_courseid[int(course_id)]),max(subject_code_to_courseid[int(temp_dict[(compre_time[0],compre_time[1])])],subject_code_to_courseid[int(course_id)]),compre_time[1],compre_time[0]])
            else:
                temp_dict[(compre_time[0],compre_time[1])]=int(course_id)

    def check_conflict(self,timing1,timing2):
        for i in timing1:
            for j in timing2:
                if i.day==j.day:
                    if i.start<=j.start<i.end or j.start<=i.start<j.end:return True  

    def authenticate_class_timings(self):
        global class_timings_conflict
        global subject_code_to_courseid
        for i in range(len(self.classtimings)):
            for j in range(i+1,len(self.classtimings)):
                if self.check_conflict(self.classtimings[i][1],self.classtimings[j][1])==True:
                    class_timings_conflict.append(["CLASS_TIMINGS_CONFLICT",self.Id,self.name,subject_code_to_courseid[int(self.classtimings[i][0][0])],self.classtimings[i][0][1],subject_code_to_courseid[int(self.classtimings[j][0][0])],self.classtimings[j][0][1]])
    
    def authenticate_unit_overdose(self):
        global units_overdose
        global course_dict
        global subject_code_to_courseid
        courses_registered = set()
        for course_id,sec in self.courseslist :
            courses_registered.add(course_id)
        units = 0
        for course_id in courses_registered :
            try:
                temp = course_dict[subject_code_to_courseid[int(course_id)]]
            except:
                temp = 3
                course_not_found.add(subject_code_to_courseid[int(course_id)])
            units += temp
 
        #print(units,courses_registered)
        self.cur_units = units
        if units > self.max_units :
            units_overdose.append(["UNITS_OVERLOADING",self.Id,self.name,units])
        
    def pprint(self):
        print(self.Id,self.name,self.courseslist,self.max_units,self.cur_units,sep='\n')
    
    def authenticate_section_clash(self):
        global subject_code_to_courseid
        global section_clash
        cl = self.courseslist
        classes=defaultdict(list)
        for i,j in cl:
            classes[str(i)+str(j)[:1]].append(str(j)[1:])
        for ind,item in classes.items():
            if len(item)!=1:
                section_clash.append(["Section_clash",self.Id,self.name,subject_code_to_courseid[int(ind[:-1])],ind[-1],*item])
        
def process(days,start,end):
	res=[]
	pos=start.find(':')
	strt=start[:pos]
	strt=int(strt)
	pos=end.find(':')
	endt=end[:pos]
	endt=int(endt)
	if end[pos+1]!='0':endt+=1
	for i in range(len(days)):
		if days[i]=='T':
			if i==len(days)-1:res.append(timing("Tue",strt,endt))
			elif days[i+1]=="H":
				i+=1
				res.append(timing("Thu",strt,endt))
			else:
				res.append(timing("Tue",strt,endt))
		elif days[i]=='M':res.append(timing("Mon",strt,endt))
		elif days[i]=='W':res.append(timing("Wed",strt,endt))
		elif days[i]=='F':res.append(timing("Fri",strt,endt))
		elif days[i]=='S':res.append(timing("Sat",strt,endt))
	return res
	
def section(row):
    lec=str(row["Lecture Section No"])
    prac=str(row["Practical Section No"])
    tut=str(row["Tutorial Section No"])
    proj=str(row["Project Section No"])
    thes=str(row["Thesis section"])
    if lec!='nan':return lec
    if prac!='nan':return prac
    if tut!='nan':return tut
    if proj!='nan':return proj
    if thes!='nan':return thes
	
	
#converting day/month/year  format entries to year-day-month format
def convert(date_compre):
    index_of_first_Dash=date_compre.find('/')
    date=date_compre[:index_of_first_Dash]
    if len(date)<2:date='0'+date
    month=date_compre[index_of_first_Dash+1:index_of_first_Dash+3]
    year=date_compre[-4:]
    new_date_compre=year+'-'+date+'-'+month
    return(new_date_compre)
	
if len(sys.argv)==4:
	timetable_file=sys.argv[1]
	reg_file=sys.argv[2]
	out_file=sys.argv[3]
elif len(sys.argv)==3:
	timetable_file=sys.argv[1]
	reg_file=sys.argv[2]
	out_file="Conflict.xlsx"
else:
	timetable_file="timetable.xlsx"
	reg_file="regdata.xlsx"
	out_file="Conflict.xlsx"
	
if os.path.isfile(out_file):os.remove(out_file)	
f=open(out_file, 'a+') #creating file if it does not exist  
f.close()

tt=pd.read_excel(timetable_file,skiprows=[0])
tt=tt[["Course ID","Exam Tm Cd","Exam Date","Subject","Catalog","Section","Class Pattern","Mtg Start","End time"]]





tt_subject_code=tt[["Course ID","Subject","Catalog"]]
tt_subject_code=tt_subject_code.drop_duplicates()

subject_code_to_courseid={}
courseid_to_subject_code={}

for i,row in tt_subject_code.iterrows():
    subject_code_to_courseid[int(row["Course ID"])]=str(row["Subject"]).strip()+" "+str(row["Catalog"]).strip()
    courseid_to_subject_code[str(row["Subject"]).strip()+" "+str(row["Catalog"]).strip()]=int(row["Course ID"])



 
#generating new dataframe for creating compre schedule
tt_compre_subset=tt[["Course ID","Exam Tm Cd","Exam Date"]]
tt_compre_subset=tt_compre_subset.dropna(how='any',subset=["Exam Tm Cd","Exam Date"])
tt_compre_subset=tt_compre_subset.drop_duplicates()

compredates={} #dict to store courseid:[compresession,compredate]

#iterating over the new compre dataframe
for index,row in tt_compre_subset.iterrows():  
    #checking if entry already exists
    course_id=int(row['Course ID'])
    compre_ssn=str(row["Exam Tm Cd"])[1:3]
    compre_date=str(row["Exam Date"])[:10]
    if '/' in compre_date:
        compre_date=convert(compre_date)
    if course_id in compredates:  
        #checking if existing entry is same as new entry
        if compredates[course_id] !=[compre_sssn,compre_date]: 
            #printing error message if new entry 
            print("Error Two Different Compre dates for Same Subject",course_id,compredates[course_id],[compre_ssn,compre_date])
    else:
         compredates[course_id]=[compre_ssn,compre_date]
           
		 
		 
tt_class_timings=tt[["Course ID","Section","Class Pattern","Mtg Start","End time"]]
tt_class_timings_1=tt_class_timings.dropna(how='any',subset=["Class Pattern","Mtg Start","End time"])
tt_class_timings_unique=tt_class_timings_1.drop_duplicates()
tt_class_timings_unique=tt_class_timings_unique.sort_values(['Course ID'])


classtimes= defaultdict(list)
for index,row in tt_class_timings_unique.iterrows():
	c_id=str(row["Course ID"])
	sec=str(row["Section"])
	days=str(row["Class Pattern"])
	strt_time=str(row["Mtg Start"])
	end_time=str(row["End time"])
	res=process(days,strt_time,end_time)
	for i in res:classtimes[(c_id,sec)].append(i)        
    




reg=pd.read_excel(reg_file,skiprows=[0])
reg=reg[["Campus ID","Name","Course ID","Lecture Section No","Practical Section No","Tutorial Section No","Project Section No","Thesis section"]]
reg=reg.dropna(how="all",subset=["Lecture Section No","Practical Section No","Tutorial Section No","Project Section No","Thesis section"])
reg["Section"]=reg.apply(lambda row:section(row),axis=1)
reg_mod=reg[["Campus ID","Name","Course ID","Section"]]
reg_mod=reg_mod.drop_duplicates()
reg_mod=reg_mod.sort_values(['Campus ID'])


student_info={}
for i,row in reg_mod.iterrows():
    stud_id=str(row["Campus ID"])
    name=str(row["Name"])
    courseid=str(row["Course ID"])
    sec=str(row["Section"])
    if stud_id not in student_info:
        student_info[stud_id]=student(stud_id,name)
        student_info[stud_id].add_course((courseid,sec))
    else:
        student_info[stud_id].add_course((courseid,sec))
        


for i,student_entry in student_info.items():
    student_entry.generate_class_timings()
    student_entry.generate_compre_dates()
    
compre_conflict=[]
class_timings_conflict=[]
units_overdose = []
section_clash = []
#student_info["2017A8PS0487G"].authenticate_section_clash()

for i,student_entry in student_info.items():
	student_entry.authenticate_compre_dates()
	student_entry.authenticate_class_timings()
	student_entry.authenticate_unit_overdose()
	student_entry.authenticate_section_clash()
	

writer=pd.ExcelWriter(out_file)

print(*course_not_found,sep='\n')

compre_df=pd.DataFrame(compre_conflict,columns=["ISSUE OF CONFLICT","ID","NAME","Course ID 1","Course ID 2","Compre date","Compre Session"])
class_timings_df=pd.DataFrame(class_timings_conflict,columns=["ISSUE OF CONFLICT","ID","NAME","Course ID 1","Course Section 1","Course ID 2","Course Section 2"])
units_df = pd.DataFrame(units_overdose,columns=["ISSUE OF CONFLICT","ID","NAME","UNITS REGISTERED"])
sec_df = pd.DataFrame(section_clash,columns = ["ISSUE OF CONFLICT","ID","NAME","Course ID","LEC/TUT","Section 1","Section 2"])
compre_df.to_excel(writer,"Compre dates",index=False)
class_timings_df.to_excel(writer,"Class Timings",index=False)
units_df.to_excel(writer,"Units Overload",index=False)
sec_df.to_excel(writer,"Section Clash",index = False)

writer.save()
