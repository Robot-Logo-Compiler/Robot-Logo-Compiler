class InputFileError():

    #   These messages are only in English, since they are only for the teacher to see
    def too_many_arguments():
        print('Too many arguments. Please provide one file of Logo code as argument.')
        raise SystemExit(0)
    
    def no_arguments():
        print('No file provided as argument. Please provide one file of Logo code as argument.')
        raise SystemExit(0)

    def file_read_error(file):
        print('Could not open file:', file, 'Please provide one file of Logo code as argument.')
        raise SystemExit(0)

class LexerError():
    def unknown_command(command): 
        print('En tunnistanut komentoa: "', command, '". Tarkista, että komento on olemassa ja että se on varmasti kirjoitettu oikein :)')
        # print('I could not recognize the command: ', command, '. Please check that the command is spelled correctly :)')
        raise SystemExit(0)

class ParserError():
    def child_is_invalid_type(keyword, input_child, correct_type, invalid_type):

        print('Komento "', keyword, '" haluaa syötteeksi "', correct_type, 
                '" mutta sen sijaan komento sai syötteeksi "', invalid_type, '".' )
        print('Pystyisitkö vaihtamaan syötteen "', input_child.return_type(), '" tilalle oikeanlaisen syötteen?')

        # print('The command "', keyword, '" wants to have an input of a "', correct_type, 
        #        '" but instead the command received an input of "', invalid_type, '".' )
        # print('Would you please change the input "', input_child, '" into a correct one?')
        raise SystemExit(0)