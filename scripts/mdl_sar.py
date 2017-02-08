#!/usr/bin/env python

import re


pdfs_file = './pdf_names_2017.txt'
sessions_file = './session_names_2017.txt'

with open(pdfs_file) as f:
    pdf_names = f.read().splitlines()

with open(sessions_file) as f:
    session_names = f.read().splitlines()

#for i in xrange(0,len(pdf_names)):
#    print str(i+1).zfill(3) + '_-_' + pdf_names[i][:-4] + '_-_' + session_names[i] + pdf_names[i][-4:]


card_pre = """
<section class="section--center mdl-grid mdl-grid--no-spacing mdl-shadow--2dp">
            <header class="section__play-btn mdl-cell mdl-cell--3-col-desktop mdl-cell--2-col-tablet mdl-cell--4-col-phone mdl-color--teal-100 mdl-color-text--white">
              <i class="material-icons">record_voice_over</i>
            </header>
            <div class="mdl-card mdl-cell mdl-cell--9-col-desktop mdl-cell--6-col-tablet mdl-cell--4-col-phone">
              <div class="mdl-card__supporting-text">
"""

card_content = """                
<h4>Incidental_Findings_-_Introduction_and_Overview</h4>
                Monday_0700_LBerland
"""

card_post_1 = """
              </div>
              <div class="mdl-card__actions">
                <a href="pdf/"""


card_post_2 = """" target="_blank" class="mdl-button">Handout</a>
              </div>
            </div>
</section>
"""

"""
<section class="section--center mdl-grid mdl-grid--no-spacing mdl-shadow--2dp">
            <header class="section__play-btn mdl-cell mdl-cell--3-col-desktop mdl-cell--2-col-tablet mdl-cell--4-col-phone mdl-color--teal-100 mdl-color-text--white">
              <i class="material-icons">record_voice_over</i>
            </header>
            <div class="mdl-card mdl-cell mdl-cell--9-col-desktop mdl-cell--6-col-tablet mdl-cell--4-col-phone">
              <div class="mdl-card__supporting-text">
                <h4>Incidental_Findings_-_Introduction_and_Overview</h4>
                Monday_0700_LBerland
              </div>
              <div class="mdl-card__actions">
                <a href="#" class="mdl-button">Handout</a>
              </div>
            </div>
</section>
"""

for i in xrange(0,len(pdf_names)):
    print card_pre + "<h4>" + session_names[i]  + "</h4>" + pdf_names[i][:-4].replace("_"," ") + card_post_1 + pdf_names[i] + card_post_2

