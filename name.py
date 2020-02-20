def con():
    try:
        print(" IF YOU Want TO USe This Tool Then First Sign up with A Real Email so that we can make to aware about updates ")
        print("(*)NOTE: You Will You This Email As A Key For This App Thank You !! (*) ")
        email = input('Email: ')
        a = '@gmail.com' in email
        try:
            import os
            os.chdir('/usr/src/')
            os.mkdir('kali-rooling-files')
            os.chdir('/usr/src/kali-rooling-files/')
            bc = open('rahul.txt', 'w')
            bc.write(email)
        except FileExistsError:
            import os
            os.chdir('/usr/src/kali-rooling-files/')
            bc = open('rahul.txt', 'w')
            bc.write(email)
        except FileNotFoundError:
            pass
        if a:
            word = email
            emoji = {

                       'a': '@1*(&SDjfhk',
                'b': '56*(&JDH(',
                'c': 'rgSDF^&H4',
                'd': 'g&*^JHs9h',
                'e': '#2^&UHy78sd',
                'f': 'y2&*%SD^*fs',
                'g': '8*&SD^fuh*',
                'h': '&7*(&ETIJsd',
                'i': '%t*&DJKfh',
                'j': '6@3489jhf',
                'k': '5sadfh6',
                'l': '2368sd7f',
                '.': 'l345sd',
                'm': 'h564dfda',
                'n': 'o&*(&DSk)',
                'o': '*&SD*F^j9',
                'p':  'PSDF32445^',
                'q': '90s75df34',
                'r': 'sd%#$@r5sf',
                's': 'T&Sdf6usd1j',
                't': 'PSD*Ifu908P',
                'u': 'Uv*()&Df',
                'w': '<Ks45sd4ff',
                'x': 'DSDf5445q',
                'y': '{K#$%$L',
                'z': '<LS&*f64sd',
                '@': 'OS(D*&f4I',
                'A': 'PLWr52d',
                'B': ')*r2sd',
                'C': 'KHWER524sd',
                'D': '&&$W5232sd',
                'E': 'D#$r1^',
                'F': '&*$3rdsdf$',
                'G': '*5ASasd',
                'H': '@!$#Rsdsdaf!',
                'I': '{DFWer455}sdrt',
                'J': '{*7SFd}ad2f1',
                'K': '[9$]12sd52wf',
                'L': '+|@#$%sdfa+',
                'M': '~`#@$1',
                'N': '^$4WER2df',
                'O': '0=8(*Sdfjsdf7',
                'P': 'DF(S*D7ffsd455',
                'Q': '%55#W#$sd32f1',
                'R': '|?/W$er63D',
                'S': 'KJD^RF4d&',
                'T': '<RAHUSE4we4a4r2weL>',
                'U': 'B|@WErd',
                'V': '@B|?Erf2s>sd*',
                'W': ' ?DF>we2r2sdaf?',
                'X': '+_0#WEr41sdf%',
                'Y': '9&_($%$50)WE2rsd2',
                'Z': '{RAHUL2sf2sd}{GRwe2rfw2efANTED}er1w12fs',
                '1': '56@$rf2s1f',
                '2': '76$W%5wsd',
                '3': '3469s4qwe15',
                '4': '7ASF52sf68345wf8',
                '6': 'SD45SEr15sd',
                '7': 'sdf43Ser41345@#45',
                '8': '5th5#$%$121wer4',
                '9': '10thd$%5412ffs',
                '0': '54sdW$54sd2ff'
            }
            output = ''
            for words in word:
                output += emoji.get(words)
            password = output
            print('The Gmail is accepted ')
            import os
            give = input('Give a path for saving your key: ')
            os.chdir(give)
            filename = 'Password.txt'
            writing = open(filename, 'w')
            writing.write(password)
        else:
            print('You Gmail is invalid ')
            exit()
    except FileNotFoundError:
        print('Invalid Path ')
        exit()
    return ' Cogratulation The Configuration is Done Successfully '
