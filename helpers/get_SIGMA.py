import math
def get_SIGMA(modulation, m_coef, SNR):
    sigma = 1
    dots_on_cvadr = m_coef/4
    
    if (modulation == 'QAM') & (m_coef == 4):
        avg = (math.sqrt(2))/dots_on_cvadr
        sigma = math.pow(10, (10*math.log10(avg) - SNR)/10)
    
    if (modulation == 'QAM') & (m_coef == 16):
        avg = (math.sqrt(2)+ 2*math.sqrt(10)+ math.sqrt(18))/dots_on_cvadr
        sigma = math.pow(10, (10*math.log10(avg) - SNR)/10)
    
    if (modulation == 'QAM') & (m_coef == 64):
        x1 = 1
        x2 = 3
        x3 = 5
        x4 = 7
        y1 = 1
        y2 = 3
        y3 = 5
        y4 = 7
        line1 = math.sqrt(x1**2 + y1**2) + math.sqrt(x2**2 + y1**2) + math.sqrt(x3**2 + y1**2) + math.sqrt(x4**2 + y1**2)
        line2 = math.sqrt(x1**2 + y2**2) + math.sqrt(x2**2 + y2**2) + math.sqrt(x3**2 + y2**2) + math.sqrt(x4**2 + y2**2)
        line3 = math.sqrt(x1**2 + y3**2) + math.sqrt(x2**2 + y3**2) + math.sqrt(x3**2 + y3**2) + math.sqrt(x4**2 + y3**2)
        line4 = math.sqrt(x1**2 + y4**2) + math.sqrt(x2**2 + y4**2) + math.sqrt(x3**2 + y4**2) + math.sqrt(x4**2 + y4**2)
        avg = (line1 + line2 + line3 + line4)/dots_on_cvadr
        sigma = math.pow(10, (10*math.log10(avg) - SNR)/10)
        
    if (modulation == 'QAM') & (m_coef == 256):
        x1 = 1
        x2 = 3
        x3 = 5
        x4 = 7
        x5 = 9
        x6 = 11
        x7 = 13
        x8 = 15
        y1 = 1
        y2 = 3
        y3 = 5
        y4 = 7
        y5 = 9
        y6 = 11
        y7 = 13
        y8 = 15
        line1 = math.sqrt(x1**2 + y1**2) + math.sqrt(x2**2 + y1**2) + math.sqrt(x3**2 + y1**2) + math.sqrt(x4**2 + y1**2) + math.sqrt(x5**2 + y1**2) + math.sqrt(x6**2 + y1**2) + math.sqrt(x7**2 + y1**2) + math.sqrt(x8**2 + y1**2)
        line2 = math.sqrt(x1**2 + y2**2) + math.sqrt(x2**2 + y2**2) + math.sqrt(x3**2 + y2**2) + math.sqrt(x4**2 + y2**2) + math.sqrt(x5**2 + y2**2) + math.sqrt(x6**2 + y2**2) + math.sqrt(x7**2 + y2**2) + math.sqrt(x8**2 + y2**2)
        line3 = math.sqrt(x1**2 + y3**2) + math.sqrt(x2**2 + y3**2) + math.sqrt(x3**2 + y3**2) + math.sqrt(x4**2 + y3**2) + math.sqrt(x5**2 + y3**2) + math.sqrt(x6**2 + y3**2) + math.sqrt(x7**2 + y3**2) + math.sqrt(x8**2 + y3**2)
        line4 = math.sqrt(x1**2 + y4**2) + math.sqrt(x2**2 + y4**2) + math.sqrt(x3**2 + y4**2) + math.sqrt(x4**2 + y4**2) + math.sqrt(x5**2 + y4**2) + math.sqrt(x6**2 + y4**2) + math.sqrt(x7**2 + y4**2) + math.sqrt(x8**2 + y4**2)
        line5 = math.sqrt(x1**2 + y5**2) + math.sqrt(x2**2 + y5**2) + math.sqrt(x3**2 + y5**2) + math.sqrt(x4**2 + y5**2) + math.sqrt(x5**2 + y5**2) + math.sqrt(x6**2 + y5**2) + math.sqrt(x7**2 + y5**2) + math.sqrt(x8**2 + y5**2)
        line6 = math.sqrt(x1**2 + y6**2) + math.sqrt(x2**2 + y6**2) + math.sqrt(x3**2 + y6**2) + math.sqrt(x4**2 + y6**2) + math.sqrt(x5**2 + y6**2) + math.sqrt(x6**2 + y6**2) + math.sqrt(x7**2 + y6**2) + math.sqrt(x8**2 + y6**2)
        line7 = math.sqrt(x1**2 + y7**2) + math.sqrt(x2**2 + y7**2) + math.sqrt(x3**2 + y7**2) + math.sqrt(x4**2 + y7**2) + math.sqrt(x5**2 + y7**2) + math.sqrt(x6**2 + y7**2) + math.sqrt(x7**2 + y7**2) + math.sqrt(x8**2 + y7**2)
        line8 = math.sqrt(x1**2 + y8**2) + math.sqrt(x2**2 + y8**2) + math.sqrt(x3**2 + y8**2) + math.sqrt(x4**2 + y8**2) + math.sqrt(x5**2 + y8**2) + math.sqrt(x6**2 + y8**2) + math.sqrt(x7**2 + y8**2) + math.sqrt(x8**2 + y8**2)
        avg = (line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8)/dots_on_cvadr
        sigma = math.pow(10, (10*math.log10(avg) - SNR)/10)
    
    #--------------------------------------------------------------
    
    if (modulation == 'PSK') & (m_coef == 2):
        sigma = math.pow(10, (10*math.log10(1) - SNR)/10)
        
    if (modulation == 'PSK') & (m_coef == 4):
        sigma = math.pow(10, (10*math.log10(1) - SNR)/10)
    
    if (modulation == 'PSK') & (m_coef == 8):
        sigma = math.pow(10, (10*math.log10(1) - SNR)/10)
        
    if (modulation == 'PSK') & (m_coef == 16):
        sigma = math.pow(10, (10*math.log10(1) - SNR)/10)
        
    if (modulation == 'PSK') & (m_coef == 32):
        sigma = math.pow(10, (10*math.log10(1) - SNR)/10)
    
    return sigma
