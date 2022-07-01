import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1124_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1124   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卢格兰老人'),
    TXT(0x02, '梅贝尔市长'),
    TXT(0x03, '雪拉扎德'),
    TXT(0x04, '奥利维尔'),
    TXT(0x05, '科洛丝'),
    TXT(0x06, '金'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1121.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x176B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02380._CH', 'ED6_DT07/CH02380P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 180,
            z                   = 0,
            y                   = 4400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0114,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x19B
@scena.Code('Init')
def Init():
    OP_B1('T1121_2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1C0',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    def _loc_1C0(): pass

    label('loc_1C0')

    Return()

# id: 0x0002 offset: 0x1C1
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    OP_6D(480, 0, 2930, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -70, 0, 2350, 0)
    SetChrPos(0x000A, -1140, 0, 2340, 0)
    SetChrPos(0x000D, -50, 0, 250, 0)
    SetChrPos(0x000C, -320, 0, 1350, 0)
    SetChrPos(0x000B, -1360, 0, 970, 0)
    SetChrPos(0x0009, 970, 0, 1880, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0380301535V#634F哎呀……\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380301536V#632F不过真没想到阿加特那家伙\n',
            '还有那样的过去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301537V#618F#4P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301538V#615F听了你们的话，\n',
            '我总算明白了',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301539V那时阿加特的\n',
            '心情是怎样的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0389')
    def lambda_0389():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0389)

    Sleep(50)

    @scena.Lambda('lambda_039C')
    def lambda_039C():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_039C)

    Sleep(50)

    @scena.Lambda('lambda_03AF')
    def lambda_03AF():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_03AF)

    Sleep(50)

    @scena.Lambda('lambda_03C2')
    def lambda_03C2():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_03C2)

    Sleep(50)

    OP_8C(0x000B, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010301540V#1004F那时？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0360301541V#612F#2P１０年前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301542V『百日战役』刚结束，\n',
            '阿加特曾经\n',
            '来过我家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301543V#1020F咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060301544V#044F#6P去了前辈的家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301545V#615F#2P嗯，他当时气势汹汹地\n',
            '逼问还身为市长的父亲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301546V身为柏斯市长，肩负统辖\n',
            '整个地方的责任……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301547V#612F可为什么要抛下\n',
            '拉文努村不管，他这样质问父亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210161V#1026F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301549V#618F#2P还是孩子的我，\n',
            '看着责备父亲的阿加特\n',
            '感到很恼火……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301550V所以忍不住就冲出去\n',
            '打了阿加特一记耳光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301551V#1007F啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030301552V#524F#6P总之，是件不幸的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301553V#618F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301554V#612F结果，家父也未能对\n',
            '阿加特的问题做出回答。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301555V而是告诉他准备把复兴村子的\n',
            '援助金送过去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301556V听完解释之后的阿加特\n',
            '将拳头指向了父亲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301557V#615F……可是，最后他把拳头放了下来，\n',
            '然后就奔跑着离开了我家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301558V#1015F有那么一回事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301559V所以阿加特和市长你，\n',
            '彼此之间有一种奇怪的氛围呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301560V#615F#2P……双方都对那时的\n',
            '事怀有芥蒂呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301561V#618F可是我没想到阿加特的\n',
            '妹妹在那场战争中丧生了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301562V我……\n',
            '好象误解了他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301563V#1025F好了，他不把事情说出来\n',
            '自己也有责任的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301564V市长你没必要太介怀的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301565V#615F#2P呵呵……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301566V#612F……阿加特的\n',
            '伤势怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301567V#1006F嗯，不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301568V过两三天就\n',
            '应该能活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380301569V#630F呼……\n',
            '可以说是不幸中的万幸了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301570V#611F#2P嗯……\n',
            '没有大碍就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301571V#618F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060301572V#043F#6P对了，前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060301573V莉拉小姐的\n',
            '情况怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301574V#618F#2P……那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301575V对伤势是做了处理，\n',
            '不过现在还没有醒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060301576V#049F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040301577V#032F嗯……\n',
            '真让人痛心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040301578V那美丽又可怜的小姐\n',
            '本应是世上最珍贵的珍宝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301579V#611F#2P呵呵……等莉拉醒了\n',
            '我会转达给她的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301580V#610F不过说起来……\n',
            '摩尔根将军说的话真能鼓励人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301581V如果军队能和协会联手的话，\n',
            '那是最令人安心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030301582V#026F#6P虽然还没有决定下来，\n',
            '所以不能轻易地下保证……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030301583V#027F不过我们会尽\n',
            '自己所能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x00C3, 0x01, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0CDA')
    def lambda_0CDA():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CDA)

    Sleep(50)

    @scena.Lambda('lambda_0CED')
    def lambda_0CED():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0CED')

    DispatchAsync2(0x0101, 0x0003, lambda_0CED)

    Sleep(50)

    @scena.Lambda('lambda_0D03')
    def lambda_0D03():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D03')

    DispatchAsync2(0x000A, 0x0003, lambda_0D03)

    Sleep(50)

    @scena.Lambda('lambda_0D19')
    def lambda_0D19():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D19')

    DispatchAsync2(0x000D, 0x0003, lambda_0D19)

    Sleep(50)

    @scena.Lambda('lambda_0D2F')
    def lambda_0D2F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D2F')

    DispatchAsync2(0x000C, 0x0003, lambda_0D2F)

    Sleep(50)

    @scena.Lambda('lambda_0D45')
    def lambda_0D45():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D45')

    DispatchAsync2(0x000B, 0x0003, lambda_0D45)

    Sleep(50)

    @scena.Lambda('lambda_0D5B')
    def lambda_0D5B():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0D5B')

    DispatchAsync2(0x0009, 0x0003, lambda_0D5B)

    Sleep(100)

    @scena.Lambda('lambda_0D71')
    def lambda_0D71():
        OP_6D(760, 0, 3570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D71)

    OP_8E(0x0008, 1940, 0, 4690, 1500, 0x00)
    OP_8C(0x0008, 0, 400)
    OP_23(0x00C3)
    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x00, 0x00)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0380301584V#630F#4P这里是游击士协会所属\n',
            '柏斯支部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380301585V#633F啊，是将军阁下。\n',
            '我们等您很久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301586V#1006F（来了来了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030301587V#027F#6P（看看……\n',
            '到底会怎么样呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380301588V#632F#4P嗯嗯……噢噢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380301589V#633F哦，真没想到会这样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380301590V#630F原来如此……\n',
            '明早10点，国际空港。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380301591V#631F我明白了。\n',
            '我会准确地传达的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_22(0x0083, 0x00, 0x64)
    OP_82(0x01, 0x00)
    Sleep(500)

    OP_8C(0x0008, 270, 400)

    @scena.Lambda('lambda_0F9A')
    def lambda_0F9A():
        OP_6D(480, 0, 2930, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0F9A)

    OP_8E(0x0008, 180, 0, 4400, 1500, 0x00)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x000A, 0x03)
    TerminateThread(0x000D, 0x03)
    TerminateThread(0x000C, 0x03)
    TerminateThread(0x0009, 0x03)
    TerminateThread(0x000B, 0x03)

    @scena.Lambda('lambda_0FDE')
    def lambda_0FDE():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FDE)

    @scena.Lambda('lambda_0FEC')
    def lambda_0FEC():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FEC)

    @scena.Lambda('lambda_0FFA')
    def lambda_0FFA():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0FFA)

    @scena.Lambda('lambda_1008')
    def lambda_1008():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1008)

    @scena.Lambda('lambda_1016')
    def lambda_1016():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1016)

    OP_8C(0x000B, 0, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010301592V#1006F怎么样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380301593V#632F王国军明日要用飞行舰队\n',
            '展开捕龙作战计划。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380301594V你们也可以以观察员的身份\n',
            '登上军舰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301595V#1004F使用飞行舰队进行捕龙作战！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040301596V#035F哇喔……\n',
            '好壮观的行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040301597V#030F那是王国军最精锐的部队吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030301598V#026F#6P虽然观察员其实\n',
            '干不了什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030301599V#027F不过能够近距离地观察龙的样子，\n',
            '老实说真是求之不得呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0080301600V#070F#4P嗯，如果军队作战失败\n',
            '就轮到我们出场了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301601V#1006F嗯……\n',
            '看来不能掉以轻心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0360301602V#611F#2P呵呵……\n',
            '总算看见一线希望了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301603V#618F…………啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(800)

    @scena.Lambda('lambda_12B8')
    def lambda_12B8():
        OP_6D(530, 0, 2880, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_12B8)

    Sleep(400)

    @scena.Lambda('lambda_12D5')
    def lambda_12D5():
        OP_6D(480, 0, 2930, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_12D5)

    Sleep(400)

    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_12F8')
    def lambda_12F8():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12F8)

    Sleep(50)

    @scena.Lambda('lambda_130B')
    def lambda_130B():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_130B)

    Sleep(50)

    @scena.Lambda('lambda_131E')
    def lambda_131E():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_131E)

    Sleep(50)

    @scena.Lambda('lambda_1331')
    def lambda_1331():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1331)

    Sleep(50)

    OP_8C(0x000B, 90, 400)

    ChrTalk(
        0x000C,
        (
            '#0060301604V#043F#6P前、前辈……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301605V#1020F怎、怎么了，市长？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301606V#617F#2P不……没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040301607V#032F刚才你好象有些头晕吧？\n',
            '你似乎很累。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301608V#618F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030301609V#524F#6P虽然知道你有很多事情，\n',
            '不过太勉强自己就不好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301610V#617F#2P呵呵……我没有勉强自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301611V#610F『百日战役』时、\n',
            '父亲采用了各种手段\n',
            '确保了柏斯市民的安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301612V有时还会为了欺骗帝国军\n',
            '而进行危险的交易。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301613V和那时相比较……\n',
            '这不算什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281488V#1026F市长先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060301615V#043F#6P梅贝尔前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0360301616V#611F#2P艾丝蒂尔小姐，还有大家。\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360301617V请为柏斯市民和\n',
            '拉文努村的大伙们消除不安吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301618V#1006F嗯……交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1211._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1668
@scena.Code('func_03_1668')
def func_03_1668():
    FadeOut(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_171F'),
        (0x00000001, 'loc_1725'),
        (-1, 'loc_172B'),
    )

    def _loc_171F(): pass

    label('loc_171F')

    OP_A2(0x1200)

    Jump('loc_172B')

    def _loc_1725(): pass

    label('loc_1725')

    OP_A2(0x1201)

    Jump('loc_172B')

    def _loc_172B(): pass

    label('loc_172B')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x00FF,
            0x00FF,
        ),
        (
            0x0002,
            0x0003,
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
