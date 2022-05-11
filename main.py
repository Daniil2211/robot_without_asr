from time import sleep
import datetime
from datetime import timedelta
import pytz

'''if __name__ == '__main__':
    import libneuro

    nn = libneuro.NeuroNetLibrary()
    nlu = libneuro.NeuroNluLibrary()
    nv = libneuro.NeuroVoiceLibrary()
    InvalidCallStateError = libneuro.InvalidCallStateError
    check_call_state = libneuro.check_call_state'''

['привет', 'как дела']
def main():
    main_online()


def main_online():
    tube_main()
    return


@check_call_state(nv)
def tube_logic(r):
    nn.log('unit', 'tube_logic')
    tube_logic_exec_count = nn.env('tube_logic_exec_count')
    if not tube_logic_exec_count:
        nn.env('tube_logic_exec_count', 1)
    else:
        tube_logic_exec_count = tube_logic_exec_count + 1
        nn.env('tube_logic_exec_count', tube_logic_exec_count)
        if tube_logic_exec_count and tube_logic_exec_count > 10:
            nn.log("Recursive execution detected")
            return
    # #1.2
    if not r:
        nn.log('condition', 'NULL')
        nn.env('result', 'NULL - молчание от клиента')
        update_common_result()
        tube_logic_NULL_NULL_count = nn.env('tube_logic_NULL_NULL_count')
        if not tube_logic_NULL_NULL_count:
            nn.env('tube_logic_NULL_NULL_count', 1)
            tube_logic_NULL_NULL_count = 1
        else:
            tube_logic_NULL_NULL_count = tube_logic_NULL_NULL_count + 1
            nn.env('tube_logic_NULL_NULL_count', tube_logic_NULL_NULL_count)
        if tube_logic_NULL_NULL_count == 1:
            tube_null_RETURN_LOGIC()
            return
        else:
            hangup_null_HANGUP()
            nn.env('recall_is_needed', 'true')
            return
        return
    # #1.3
    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        # call_number = nn.env('call_number')
        # if not call_number:
        #    call_number = '1'
        # if call_number == '1':
        #    hello_main_1_RETURN_LOGIC()
        #    return
        # else:
        #    hello_main_2_RETURN_LOGIC()
        #    return
        ### non - voice - mail - attempt ###
        non_voice_mail_attempt = nn.env('non_voice_mail_attempt')
        if not non_voice_mail_attempt:
            non_voice_mail_attempt = 0
        if non_voice_mail_attempt == 0:
            hello_main_1_RETURN_LOGIC()
        else:
            hello_main_2_RETURN_LOGIC()
        ### non - voice - mail - attempt ###

    # #1.4
    if r.has_entity('voicemail'):
        if r.entity('voicemail') == 'true':
            nn.log('condition', 'voicemail=="true"')
            nn.env('result', 'автоответчик')
            update_common_result()
            nv.hangup()
            nn.env('recall_is_needed', 'true')
            return


# #1.1
# Здравствуйте!
@check_call_state(nv)
def tube_main():
    nv.set_default('listen', {'interruption_no_input_timeout': 1000,
                              'no_input_timeout': 6500,
                              'recognition_timeout': 60000,
                              'speech_complete_timeout': 950,
                              'start_timeout ': 0,
                              'asr_complete_timeout': 5000})
    nn.log('unit', 'tube_main')
    with nv.listen(('voicemail', None, 25, 'OR'),
                   entities=['voicemail']) as r:
        nv.say('tube_main')
    #скрипт который находит строки по регексам
    return tube_logic(r)
    pass


# #1.2
# Алло..., меня слышно?
@check_call_state(nv)
def tube_null_RETURN_LOGIC(*additional_phrases):
    nv.set_default('listen', {'interruption_no_input_timeout': 1000,
                              'no_input_timeout': 6500,
                              'recognition_timeout': 60000,
                              'speech_complete_timeout': 950,
                              'start_timeout ': 0,
                              'asr_complete_timeout': 5000})
    nn.log('unit', 'tube_null')
    with nv.listen(('voicemail', None, 35, 'OR'),
                   entities=['voicemail']) as r:
        for phrase in additional_phrases:
            nv.say(phrase)
        nv.say('tube_null')
    return tube_logic(r)
    pass




