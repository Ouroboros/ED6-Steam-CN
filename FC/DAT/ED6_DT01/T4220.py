import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4220_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4220   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '凯诺娜上尉'),
    TXT(0x02, '洛伦斯少尉'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '特务兵'),
    TXT(0x07, '卡西乌斯'),
    TXT(0x08, '摩尔根将军'),
    TXT(0x09, '艾莉茜雅女王'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4220.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xDA1
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02013._CH', 'ED6_DT07/CH02013P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            direction           = 180,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 40,
            z                   = 750,
            y                   = 155220,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x212
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_220',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0006)

    def _loc_220(): pass

    label('loc_220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24A',
    )

    SetChrChipByIndex(0x0000, 0)
    SetChrChipByIndex(0x0001, 1)
    SetChrChipByIndex(0x0138, 2)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)

    def _loc_24A(): pass

    label('loc_24A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_254',
    )

    Jump('loc_2B4')

    def _loc_254(): pass

    label('loc_254')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_28F',
    )

    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000E, 530, 0, 150340, 0)
    SetChrPos(0x000F, -400, 0, 150340, 0)

    Jump('loc_2B4')

    def _loc_28F(): pass

    label('loc_28F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_299',
    )

    Jump('loc_2B4')

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_2A3',
    )

    Jump('loc_2B4')

    def _loc_2A3(): pass

    label('loc_2A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_2AD',
    )

    Jump('loc_2B4')

    def _loc_2AD(): pass

    label('loc_2AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_2B4',
    )

    def _loc_2B4(): pass

    label('loc_2B4')

    Return()

# id: 0x0001 offset: 0x2B5
@scena.Code('Init')
def Init():
    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x2BF
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_426')

    def _loc_2E4(): pass

    label('loc_2E4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FD',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_426')

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_316',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_426')

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32F',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_426')

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_348',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_426')

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_361',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_426')

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_426')

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_393',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_426')

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AC',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_426')

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_426')

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_426')

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_426')

    def _loc_3F7(): pass

    label('loc_3F7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_410',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_426')

    def _loc_410(): pass

    label('loc_410')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_426',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_426(): pass

    label('loc_426')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_43B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_426')

    def _loc_43B(): pass

    label('loc_43B')

    Return()

# id: 0x0003 offset: 0x43C
@scena.Code('func_03_43C')
def func_03_43C():
    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_461',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_47C')

    def _loc_461(): pass

    label('loc_461')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_477',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_47C')

    def _loc_477(): pass

    label('loc_477')

    SetChrSubChip(0x00FE, 2)

    def _loc_47C(): pass

    label('loc_47C')

    SetChrDirection(0x00FE, 180, 0)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0010,
        (
            '#0630140653V#090F让曾经辞退了军衔的\n',
            '卡西乌斯阁下恢复原职，\n',
            '我心里很是过意不去啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630140654V不过有他在的话，\n',
            '我也安心了不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630140655V虽然对你们深感抱歉，\n',
            '但请暂时让你们的父亲助我一臂之力吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x554
@scena.Code('func_04_554')
def func_04_554():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5C0',
    )

    ChrTalk(
        0x000E,
        (
            '#0160140635V#080F我一会儿要去参加预定的会议。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140634V你们两个就在王都里面\n',
            '好好地玩一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63D')

    def _loc_5C0(): pass

    label('loc_5C0')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000E,
        (
            '#0160140632V#080F大街那边很热闹吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140633V我一会儿要去参加预定的会议。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140634V你们两个就在王都里面\n',
            '好好地玩一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63D(): pass

    label('loc_63D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x641
@scena.Code('func_05_641')
def func_05_641():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_681',
    )

    ChrTalk(
        0x000F,
        (
            '#0600140652V#163F理查德……\n',
            '……那个愚蠢的小子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_904')

    def _loc_681(): pass

    label('loc_681')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000F,
        (
            '#0600140637V#161F是你们俩啊……好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140638V#004F啊……摩尔根将军？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140639V#010F很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600140640V#163F是你们在艾尔贝离宫救了我的孙女吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140641V#505F艾尔贝离宫……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140642V#001F啊，是莉安妮小妹妹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140643V#010F那是我们理应要做的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140644V因为保证市民的安全是游击士的义务。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600140645V#160F哼，还是那么能说会道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600140646V不过你们不仅解放了离宫，\n',
            '而且还救出了女王陛下，\n',
            '并夺回了格兰赛尔城……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600140647V这回我真的要向你们表示感激。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140648V#002F摩尔根将军……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600140649V#160F作为游击士，\n',
            '你们做得很不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140650V#505F怎、怎么感觉您话中有话呢～\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140651V#000F算了，这样也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_904(): pass

    label('loc_904')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x908
@scena.Code('func_06_908')
def func_06_908():
    EventBegin(0x00)
    CameraMove(-400, 500, 150910, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0008, 380, 500, 150540, 270)
    SetChrPos(0x0009, -1300, 500, 151320, 138)
    SetChrPos(0x000A, -1070, 0, 147120, 0)
    SetChrPos(0x000B, 750, 0, 147120, 0)
    SetChrPos(0x000C, -1190, 0, 145180, 0)
    SetChrPos(0x000D, 820, 0, 145210, 0)

    ChrTalk(
        0x0008,
        (
            '#180F这、这究竟是怎么回事！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610130918V与『艾尔贝离宫』\n',
            '的联络竟然中断了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#280F亲卫队和游击士协会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0141070015V很有可能被其中\n',
            '之一给攻陷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F厚、厚颜无耻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610130924V指挥那里的部队的……\n',
            '少尉，不就是你吗！　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140130926V#280F我真是颜面尽失啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0141070016V不过，既然事已至此\n',
            '怎么埋怨都也已经没用了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0141070017V而且我们还必须坚守王城，\n',
            '不能让陛下被他们劫走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F不、不用你说，\n',
            '我也明白这一点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B6E')
    def lambda_0B6E():
        CameraMove(520, 0, 148610, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B6E)

    SetChrDirection(0x0008, 180, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#180F彻底封锁城门！\n',
            '无论是谁都不许入内！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610130933V然后只要准备对抗\n',
            '从空中而来的袭击就可以了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F还有，联络各地的部队\n',
            '让他们向艾尔贝离宫进发！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0611100007V理由是：镇压假冒\n',
            '王族的恐怖集团！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            'Ｙｅｓ，Ｍａｄａｍ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C7E')
    def lambda_0C7E():
        ChrWalkTo(0x00FE, 190, 0, 110220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0C7E)

    @scena.Lambda('lambda_0C99')
    def lambda_0C99():
        ChrWalkTo(0x00FE, 190, 0, 110220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0C99)

    Sleep(300)

    @scena.Lambda('lambda_0CB9')
    def lambda_0CB9():
        ChrWalkTo(0x00FE, 190, 0, 110220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CB9)

    @scena.Lambda('lambda_0CD4')
    def lambda_0CD4():
        ChrWalkTo(0x00FE, 190, 0, 110220, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CD4)

    Sleep(1000)

    CameraMove(-400, 500, 150910, 1000)

    ChrTalk(
        0x0009,
        (
            '#0140130940V#280F呵呵，很有一手嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F哼哼，那是当然。\n',
            '不要把我和你这个新来的相提并论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……阁下不在，我们\n',
            '一定要把这里守住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4300._SN', 101, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
