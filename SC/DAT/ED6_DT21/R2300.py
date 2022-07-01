import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '米克'),
    TXT(0x02, '剑齿虎'),
    TXT(0x03, '剑齿虎'),
    TXT(0x04, '梅威海道方向'),
    TXT(0x05, '杰尼丝王立学院方向'),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2300.x'
    header.mapIndex       = 102
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1D59
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
        ('ED6_DT09/CH10520._CH', 'ED6_DT09/CH10520P._CP'),
        ('ED6_DT09/CH10521._CH', 'ED6_DT09/CH10521P._CP'),
        ('ED6_DT29/CH12040._CH', 'ED6_DT29/CH12040P._CP'),
        ('ED6_DT29/CH12041._CH', 'ED6_DT29/CH12041P._CP'),
        ('ED6_DT09/CH10340._CH', 'ED6_DT09/CH10340P._CP'),
        ('ED6_DT09/CH10341._CH', 'ED6_DT09/CH10341P._CP'),
        ('ED6_DT09/CH11040._CH', 'ED6_DT09/CH11040P._CP'),
        ('ED6_DT09/CH11041._CH', 'ED6_DT09/CH11041P._CP'),
        ('ED6_DT09/CH11070._CH', 'ED6_DT09/CH11070P._CP'),
        ('ED6_DT09/CH11071._CH', 'ED6_DT09/CH11071P._CP'),
        ('ED6_DT09/CH11080._CH', 'ED6_DT09/CH11080P._CP'),
        ('ED6_DT09/CH11081._CH', 'ED6_DT09/CH11081P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT29/CH12900._CH', 'ED6_DT29/CH12900P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -31370,
            z                   = 0,
            y                   = 1980,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 119440,
            z                   = 0,
            y                   = -7810,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 8930,
            z           = 370,
            y           = 11870,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0191,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 55220,
            z           = -110,
            y           = 8450,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0195,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 87920,
            z           = 100,
            y           = 10050,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0193,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 93230,
            z           = 60,
            y           = 5930,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0194,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x22A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -11190,
            y           = -1000,
            z           = -5490,
            range       = -8710,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000189C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10005 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x24A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x24B
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEBBC8, 0xFFFE0C00, 0x00230029)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x197),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_288',
    )

    Call(0, 0x0003)

    Jump('loc_28C')

    def _loc_288(): pass

    label('loc_288')

    Call(0, 0x0002)

    def _loc_28C(): pass

    label('loc_28C')

    Return()

# id: 0x0002 offset: 0x28D
@scena.Code('ReInit')
def ReInit():
    OP_D2(0x002601B0, 0x002601B5, 0x0E)
    OP_D2(0x002601B0, 0x002601B5, 0x0F)
    OP_D2(0x00270110, 0x00270120, 0x10)
    OP_D2(0x00270112, 0x00270122, 0x11)
    OP_D2(0x00270130, 0x00270140, 0x12)
    OP_D2(0x00270131, 0x00270141, 0x13)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2E2'),
        (0x00000005, 'loc_2F9'),
        (0x00000006, 'loc_310'),
        (0x00000007, 'loc_327'),
        (-1, 'loc_33E'),
    )

    def _loc_2E2(): pass

    label('loc_2E2')

    OP_D2(0x000701D0, 0x000701DC, 0x14)
    OP_D2(0x000701D1, 0x000701DD, 0x15)

    Jump('loc_33E')

    def _loc_2F9(): pass

    label('loc_2F9')

    OP_D2(0x00070218, 0x00070224, 0x14)
    OP_D2(0x00070219, 0x00070225, 0x15)

    Jump('loc_33E')

    def _loc_310(): pass

    label('loc_310')

    OP_D2(0x00070230, 0x0007023C, 0x14)
    OP_D2(0x00070231, 0x0007023D, 0x15)

    Jump('loc_33E')

    def _loc_327(): pass

    label('loc_327')

    OP_D2(0x00070248, 0x00070254, 0x14)
    OP_D2(0x00070249, 0x00070255, 0x15)

    Jump('loc_33E')

    def _loc_33E(): pass

    label('loc_33E')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_357'),
        (0x00000005, 'loc_36E'),
        (0x00000006, 'loc_385'),
        (0x00000007, 'loc_39C'),
        (-1, 'loc_3B3'),
    )

    def _loc_357(): pass

    label('loc_357')

    OP_D2(0x000701D0, 0x000701DC, 0x16)
    OP_D2(0x000701D1, 0x000701DD, 0x17)

    Jump('loc_3B3')

    def _loc_36E(): pass

    label('loc_36E')

    OP_D2(0x00070218, 0x00070224, 0x16)
    OP_D2(0x00070219, 0x00070225, 0x17)

    Jump('loc_3B3')

    def _loc_385(): pass

    label('loc_385')

    OP_D2(0x00070230, 0x0007023C, 0x16)
    OP_D2(0x00070231, 0x0007023D, 0x17)

    Jump('loc_3B3')

    def _loc_39C(): pass

    label('loc_39C')

    OP_D2(0x00070248, 0x00070254, 0x16)
    OP_D2(0x00070249, 0x00070255, 0x17)

    Jump('loc_3B3')

    def _loc_3B3(): pass

    label('loc_3B3')

    OP_D2(0x00290387, 0x0029038B, 0x18)
    OP_D2(0x00270111, 0x00270121, 0x19)
    OP_D2(0x00290389, 0x0029038D, 0x1A)

    Return()

# id: 0x0003 offset: 0x3D2
@scena.Code('func_03_3D2')
def func_03_3D2():
    OP_D2(0x00270110, 0x00270120, 0x0E)
    OP_D2(0x00270110, 0x00270120, 0x0F)
    OP_D2(0x00270110, 0x00270120, 0x10)
    OP_D2(0x00270110, 0x00270120, 0x11)
    OP_D2(0x00270130, 0x00270140, 0x12)
    OP_D2(0x00270130, 0x00270140, 0x13)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_427'),
        (0x00000005, 'loc_43E'),
        (0x00000006, 'loc_455'),
        (0x00000007, 'loc_46C'),
        (-1, 'loc_483'),
    )

    def _loc_427(): pass

    label('loc_427')

    OP_D2(0x000701D0, 0x000701DC, 0x14)
    OP_D2(0x000701D0, 0x000701DC, 0x15)

    Jump('loc_483')

    def _loc_43E(): pass

    label('loc_43E')

    OP_D2(0x00070218, 0x00070224, 0x14)
    OP_D2(0x00070218, 0x00070224, 0x15)

    Jump('loc_483')

    def _loc_455(): pass

    label('loc_455')

    OP_D2(0x00070230, 0x0007023C, 0x14)
    OP_D2(0x00070230, 0x0007023C, 0x15)

    Jump('loc_483')

    def _loc_46C(): pass

    label('loc_46C')

    OP_D2(0x00070248, 0x00070254, 0x14)
    OP_D2(0x00070248, 0x00070254, 0x15)

    Jump('loc_483')

    def _loc_483(): pass

    label('loc_483')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_49C'),
        (0x00000005, 'loc_4B3'),
        (0x00000006, 'loc_4CA'),
        (0x00000007, 'loc_4E1'),
        (-1, 'loc_4F8'),
    )

    def _loc_49C(): pass

    label('loc_49C')

    OP_D2(0x000701D0, 0x000701DC, 0x16)
    OP_D2(0x000701D0, 0x000701DC, 0x17)

    Jump('loc_4F8')

    def _loc_4B3(): pass

    label('loc_4B3')

    OP_D2(0x00070218, 0x00070224, 0x16)
    OP_D2(0x00070218, 0x00070224, 0x17)

    Jump('loc_4F8')

    def _loc_4CA(): pass

    label('loc_4CA')

    OP_D2(0x00070230, 0x0007023C, 0x16)
    OP_D2(0x00070230, 0x0007023C, 0x17)

    Jump('loc_4F8')

    def _loc_4E1(): pass

    label('loc_4E1')

    OP_D2(0x00070248, 0x00070254, 0x16)
    OP_D2(0x00070248, 0x00070254, 0x17)

    Jump('loc_4F8')

    def _loc_4F8(): pass

    label('loc_4F8')

    OP_D2(0x00290387, 0x0029038B, 0x18)

    Return()

# id: 0x0004 offset: 0x503
@scena.Code('func_04_503')
def func_04_503():
    Call(0, 0x0005)
    Call(0, 0x0006)

    Return()

# id: 0x0005 offset: 0x50C
@scena.Code('func_05_50C')
def func_05_50C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_519',
    )

    Return()

    def _loc_519(): pass

    label('loc_519')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_539',
    )

    Call(0, 0x0010)
    Call(0, 0x0011)
    FadeIn(0, 0)

    def _loc_539(): pass

    label('loc_539')

    OP_A3(0x2031)
    OP_A3(0x2032)
    OP_A3(0x2033)
    OP_A3(0x2034)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_555',
    )

    OP_A2(0x2031)

    def _loc_555(): pass

    label('loc_555')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_565',
    )

    OP_A2(0x2032)

    def _loc_565(): pass

    label('loc_565')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_575',
    )

    OP_A2(0x2033)

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_585',
    )

    OP_A2(0x2034)

    def _loc_585(): pass

    label('loc_585')

    Fade(1000)
    SetChrPos(0x0101, -10370, 0, 1110, 90)
    SetChrPos(0x0102, -10310, 0, 90, 90)
    SetChrPos(0x00F9, -11900, 0, 1000, 90)
    SetChrPos(0x00F8, -11900, 0, -440, 90)
    OP_6D(-10660, 0, 480, 0)
    OP_67(0, 8290, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrPos(0x0008, 6950, -50, 900, 0)

    NpcTalk(
        0x0008,
        '少年的声音',
        (
            '#1900360481V#3P呜哇啊啊啊啊～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B3',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_6F1')

    def _loc_6B3(): pass

    label('loc_6B3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DA',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_6F1')

    def _loc_6DA(): pass

    label('loc_6DA')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_6F1(): pass

    label('loc_6F1')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_71D',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_75B')

    def _loc_71D(): pass

    label('loc_71D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_744',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_75B')

    def _loc_744(): pass

    label('loc_744')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_75B(): pass

    label('loc_75B')

    Sleep(1000)

    OP_21()
    OP_1D(0x29)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360482V#1004F#5P刚才那是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360483V#1042F#6P赶快、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 25)
    SetChrChipByIndex(0x0102, 18)
    SetChrChipByIndex(0x00F9, 22)
    SetChrChipByIndex(0x00F8, 20)
    SetChrFlags(0x0101, 0x1000)

    @scena.Lambda('lambda_07DD')
    def lambda_07DD():
        OP_91(0x00FE, 10000, 0, 1000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_07DD)

    Sleep(100)

    @scena.Lambda('lambda_07FD')
    def lambda_07FD():
        OP_91(0x00FE, 10000, 0, 1000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_07FD)

    Sleep(20)

    @scena.Lambda('lambda_081D')
    def lambda_081D():
        OP_91(0x00FE, 10000, 0, 1000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_081D)

    Sleep(100)

    @scena.Lambda('lambda_083D')
    def lambda_083D():
        OP_91(0x00FE, 10000, 0, 1000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_083D)

    Sleep(1000)

    Fade(1000)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F9, 0x00)
    TerminateThread(0x00F8, 0x00)
    SetChrChipByIndex(0x0102, 18)
    SetChrChipByIndex(0x00F9, 20)
    SetChrChipByIndex(0x00F8, 22)
    FormationAddMember(ChrTable['米克'], 0xFF, 0xFF)
    SetChrFlags(0x014C, 0x0008)
    OP_6D(107510, 0, -6820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 115040, 0, -7820, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x1000)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    @scena.Lambda('lambda_08F4')
    def lambda_08F4():
        OP_8E(0x00FE, 98950, 0, -6690, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_08F4)

    OP_0D()

    @scena.Lambda('lambda_0910')
    def lambda_0910():
        OP_6D(99000, 0, -6480, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0910)

    WaitForThreadExit(0x0008, 0x0001)
    OP_63(0x0008)

    @scena.Lambda('lambda_0930')
    def lambda_0930():
        OP_96(0x00FE, 0x00018060, 0x00000000, 0xFFFFE5DE, 0x0000012C, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0930)

    SetChrChipByIndex(0x0008, 14)
    SetChrSubChip(0x0008, 0)
    WaitForThreadExit(0x0008, 0x0001)
    OP_22(0x020C, 0x00, 0x50)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#1900360484V#2P啊呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    SetChrSubChip(0x0008, 1)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1900360485V#2P可、可恶……\n',
            '怎么会这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360486V得、得赶快报告……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0193, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x0008, 2)
    Sleep(500)

    Fade(500)
    OP_6D(103940, 0, -7410, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(98000, 0)
    OP_6E(434, 0)
    CreateThread(0x0009, 0x01, 0x00, 0x000B)
    CreateThread(0x000A, 0x01, 0x00, 0x000C)
    CreateThread(0x0009, 0x03, 0x00, 0x0007)
    SetChrSubChip(0x0008, 1)
    SetChrFlags(0x0008, 0x0020)
    OP_8C(0x0008, 90, 500)
    ClearChrFlags(0x0008, 0x0020)
    SetChrSubChip(0x0008, 1)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#1900360487V呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    LoadEffect(0x00, 'scraft\\\\sc000_11.eff')

    @scena.Lambda('lambda_0ADB')
    def lambda_0ADB():
        OP_6D(101140, 500, -5910, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0ADB)

    @scena.Lambda('lambda_0AF3')
    def lambda_0AF3():
        OP_67(0, 7530, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AF3)

    @scena.Lambda('lambda_0B0B')
    def lambda_0B0B():
        OP_6B(1500, 1200)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0B0B)

    @scena.Lambda('lambda_0B1B')
    def lambda_0B1B():
        OP_6C(45000, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0B1B)

    @scena.Lambda('lambda_0B2B')
    def lambda_0B2B():
        OP_6E(434, 1200)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0B2B)

    CreateThread(0x0009, 0x01, 0x00, 0x000A)
    CreateThread(0x0009, 0x03, 0x00, 0x0007)

    @scena.Lambda('lambda_0B49')
    def lambda_0B49():
        OP_6D(101940, 0, -7410, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B49)

    SetChrPos(0x0101, 91500, -10, -5720, 90)
    SetChrPos(0x0102, 91120, -30, -6800, 90)
    SetChrPos(0x00F9, 90660, 30, -5210, 90)
    SetChrPos(0x00F8, 90530, 300, -7050, 90)
    SetChrChipByIndex(0x0102, 18)
    SetChrChipByIndex(0x00F9, 22)
    SetChrChipByIndex(0x00F8, 20)
    CreateThread(0x0102, 0x01, 0x00, 0x000D)
    CreateThread(0x00F9, 0x01, 0x00, 0x000E)
    CreateThread(0x00F8, 0x01, 0x00, 0x000F)
    SetChrSubChip(0x0101, 0)

    @scena.Lambda('lambda_0BCE')
    def lambda_0BCE():
        OP_8F(0x00FE, 96310, 0, -6000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0BCE)

    WaitForThreadExit(0x0101, 0x0003)
    SetChrChipByIndex(0x0101, 17)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_0BF8')
    def lambda_0BF8():
        OP_96(0x00FE, 0x00018A9C, 0x00000000, 0xFFFFE5AC, 0x000009C4, 0x00001770)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0BF8)

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010360488V#1005F#1P喝啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_0C40')
    def lambda_0C40():
        OP_99(0x00FE, 0x00, 0x09, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C40)

    OP_22(0x01F4, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0009, 0, 1000, 0, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CreateThread(0x0009, 0x01, 0x00, 0x0009)
    WaitForThreadExit(0x0101, 0x0002)
    OP_22(0x00D5, 0x00, 0x64)

    @scena.Lambda('lambda_0CB6')
    def lambda_0CB6():
        OP_99(0x00FE, 0x09, 0x0C, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0CB6)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0008, 0x0000)
    CreateThread(0x000A, 0x01, 0x00, 0x0008)

    @scena.Lambda('lambda_0CD7')
    def lambda_0CD7():
        OP_6D(103750, 0, -6570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0CD7)

    @scena.Lambda('lambda_0CEF')
    def lambda_0CEF():
        OP_67(0, 8020, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CEF)

    @scena.Lambda('lambda_0D07')
    def lambda_0D07():
        OP_6B(1810, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0D07)

    @scena.Lambda('lambda_0D17')
    def lambda_0D17():
        OP_6E(505, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0D17)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    SetChrSubChip(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#1900360489V你，你们……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360490V#1005F#5P稍后再说！\n',
            '现在先击退这些家伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360491V#1042F#6P快退下。\n',
            '被卷进来就危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E2E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070360492V#065F#6P为、为什么这种地方\n',
            '会有『结社』的装甲兽……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC9')

    def _loc_E2E(): pass

    label('loc_E2E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E82',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360493V#022F#6P为什么这种地方\n',
            '会有『结社』的装甲兽……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC9')

    def _loc_E82(): pass

    label('loc_E82')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EC9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360494V#057F#6P为什么这种地方\n',
            '会有装甲兽……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC9(): pass

    label('loc_EC9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EFE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360495V#076F#6P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F65')

    def _loc_EFE(): pass

    label('loc_EFE')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F33',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360496V#054F#6P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F65')

    def _loc_F33(): pass

    label('loc_F33')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F65',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360497V#024F#6P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F65(): pass

    label('loc_F65')

    @scena.Lambda('lambda_0F6B')
    def lambda_0F6B():
        OP_6D(104360, 0, -6540, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F6B)

    @scena.Lambda('lambda_0F83')
    def lambda_0F83():
        OP_6B(1650, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F83)

    SetChrChipByIndex(0x0009, 24)
    CreateThread(0x0009, 0x03, 0x00, 0x0007)

    @scena.Lambda('lambda_0F9F')
    def lambda_0F9F():
        OP_91(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0F9F)

    SetChrChipByIndex(0x0101, 25)
    SetChrFlags(0x0101, 0x1000)

    @scena.Lambda('lambda_0FC4')
    def lambda_0FC4():
        OP_91(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0FC4)

    @scena.Lambda('lambda_0FDF')
    def lambda_0FDF():
        OP_91(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0FDF)

    Sleep(50)

    SetChrChipByIndex(0x000A, 24)

    @scena.Lambda('lambda_1004')
    def lambda_1004():
        OP_91(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1004)

    @scena.Lambda('lambda_101F')
    def lambda_101F():
        OP_91(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_101F)

    @scena.Lambda('lambda_103A')
    def lambda_103A():
        OP_91(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_103A)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000197, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrStatus(0x00FF, 0xF9, 0)

    Return()

# id: 0x0006 offset: 0x107F
@scena.Code('func_06_107F')
def func_06_107F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_108C',
    )

    Return()

    def _loc_108C(): pass

    label('loc_108C')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    FormationDelMember(0x4B, 0xFF)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    Sleep(500)

    OP_1D(0x15)
    OP_6D(104070, 0, -6980, 0)
    OP_67(0, 8710, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(317, 0)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrPos(0x0101, 103920, 0, -6740, 90)
    SetChrPos(0x0102, 103800, 0, -8039, 90)
    SetChrPos(0x00F9, 102580, 0, -6370, 90)
    SetChrPos(0x00F8, 102590, 0, -8440, 90)
    SetChrPos(0x0008, 98440, 0, -7170, 90)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0101, 16)
    SetChrChipByIndex(0x0102, 18)
    SetChrChipByIndex(0x00F9, 22)
    SetChrChipByIndex(0x00F8, 20)
    SetChrChipByIndex(0x0008, 12)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    SetChrSubChip(0x0008, 0)
    FadeIn(2000, 0)
    OP_0D()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F8, 0)
    SetChrSubChip(0x00F9, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010360498V#1007F呼……\n',
            '很强的装甲兽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360499V#1035F#6P啊啊……\n',
            '幸好总算赶上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1900360500V#6P得、得救了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_125B')
    def lambda_125B():
        OP_6D(103000, 0, -6950, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_125B)

    OP_8E(0x0008, 100440, 0, -7300, 3000, 0x00)

    @scena.Lambda('lambda_1287')
    def lambda_1287():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1287)

    Sleep(50)

    @scena.Lambda('lambda_129A')
    def lambda_129A():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_129A)

    Sleep(60)

    @scena.Lambda('lambda_12AD')
    def lambda_12AD():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_12AD)

    Sleep(70)

    OP_8C(0x0101, 270, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#1900360501V#6P艾丝蒂尔……\n',
            '还有约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360502V不好意思……\n',
            '危急之时承蒙相救……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360503V#1006F#2P嗯，这就是我们的\n',
            '工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360504V#1042F#2P话说回来……\n',
            '到底发生了什么事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360505V刚才的魔兽，一般来说\n',
            '可不会出现在这里的哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1900360506V#6P其、其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1900360507V#6P学院……\n',
            '王立学院被袭击了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_145D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_149B')

    def _loc_145D(): pass

    label('loc_145D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1484',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_149B')

    def _loc_1484(): pass

    label('loc_1484')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_149B(): pass

    label('loc_149B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C7',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1505')

    def _loc_14C7(): pass

    label('loc_14C7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14EE',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1505')

    def _loc_14EE(): pass

    label('loc_14EE')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1505(): pass

    label('loc_1505')

    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_1D(0x6E)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360508V#1005F#2P什…什么…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15AF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360509V#022F#2P……请说清楚点儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1624')

    def _loc_15AF(): pass

    label('loc_15AF')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360510V#057F#2P……说清楚点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1624')

    def _loc_15E8(): pass

    label('loc_15E8')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1624',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360511V#072F#2P……能说清楚点儿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1624(): pass

    label('loc_1624')

    ChrTalk(
        0x0008,
        (
            '#1900360512V#6P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360513V我……和平时一样\n',
            '在校舍后面跷课。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360514V穿红色装甲的士兵们\n',
            '突然从正门闯了进来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360515V勤务员大叔\n',
            '打算拦住他们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360516V但、但他们用枪……\n',
            '打、打伤了大叔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1761',
    )

    ChrTalk(
        0x0107,
        (
            '#0070360517V#065F#2P…………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360518V#1020F#2P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_181A')

    def _loc_1761(): pass

    label('loc_1761')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17BF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360518V#1020F#2P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080360520V#072F#2P糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_181A')

    def _loc_17BF(): pass

    label('loc_17BF')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_181A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010360518V#1020F#2P怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360522V#057F#2P不妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_181A(): pass

    label('loc_181A')

    ChrTalk(
        0x0008,
        (
            '#1900360523V#6P我一看到这个情景……\n',
            '脑子就一片空白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360524V想着要去找人帮忙\n',
            '就逃到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360525V#1035F#2P……情况了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360526V#1040F你能继续前往卢安\n',
            '帮我们转告协会吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360527V我们直接到\n',
            '学院附近看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1900360528V#6P知、知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360529V那些家伙们，除了刚才的魔兽之外，\n',
            '还带着奇怪的人形机甲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1900360530V你们要多加小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T2500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x19B1
@scena.Code('func_07_19B1')
def func_07_19B1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_19D1',
    )

    OP_22(0x013F, 0x00, 0x50)
    Sleep(150)

    OP_22(0x013F, 0x00, 0x50)
    Sleep(300)

    Jump('func_07_19B1')

    def _loc_19D1(): pass

    label('loc_19D1')

    Return()

# id: 0x0008 offset: 0x19D2
@scena.Code('func_08_19D2')
def func_08_19D2():
    SetChrChipByIndex(0x00FE, 24)
    OP_96(0x00FE, 0x0001A838, 0x0000012C, 0xFFFFDE9A, 0x000001F4, 0x00001388)
    SetChrChipByIndex(0x00FE, 13)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0009 offset: 0x19F9
@scena.Code('func_09_19F9')
def func_09_19F9():
    TerminateThread(0x00FE, 0x02)
    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 26)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1A12')
    def lambda_1A12():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00000BB8, 0x0000012C)
        Yield()

        Jump('lambda_1A12')

    DispatchAsync2(0x00FE, 0x0003, lambda_1A12)

    OP_96(0x00FE, 0x00019C94, 0x00000000, 0xFFFFE69C, 0x00000064, 0x00002710)
    TerminateThread(0x00FE, 0x03)
    ClearChrFlags(0x00FE, 0x0020)
    TerminateThread(0x00FE, 0x03)
    SetChrChipByIndex(0x00FE, 13)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1A5D')
    def lambda_1A5D():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_1A5D')

    DispatchAsync2(0x0009, 0x0002, lambda_1A5D)

    OP_22(0x023B, 0x00, 0x64)
    OP_96(0x00FE, 0x0001A7D4, 0x0000012C, 0xFFFFE82C, 0x000003E8, 0x00001770)
    OP_22(0x00A4, 0x00, 0x64)

    Return()

# id: 0x000A offset: 0x1A8C
@scena.Code('func_0A_1A8C')
def func_0A_1A8C():
    SetChrChipByIndex(0x00FE, 24)

    @scena.Lambda('lambda_1A97')
    def lambda_1A97():
        OP_99(0x00FE, 0x00, 0x07, 0x000009C4)
        Yield()

        Jump('lambda_1A97')

    DispatchAsync2(0x00FE, 0x0002, lambda_1A97)

    OP_8F(0x00FE, 103770, 0, -6690, 5000, 0x00)
    TerminateThread(0x0009, 0x03)
    SetChrChipByIndex(0x00FE, 13)
    SetChrSubChip(0x00FE, 0)
    OP_22(0x023B, 0x00, 0x64)
    OP_96(0x00FE, 0x00018A88, 0x00000000, 0xFFFFE5DE, 0x000006A4, 0x00000FA0)

    Return()

# id: 0x000B offset: 0x1AE3
@scena.Code('func_0B_1AE3')
def func_0B_1AE3():
    SetChrPos(0x00FE, 119000, 500, -6800, 270)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 24)

    @scena.Lambda('lambda_1B09')
    def lambda_1B09():
        OP_99(0x00FE, 0x00, 0x07, 0x000009C4)
        Yield()

        Jump('lambda_1B09')

    DispatchAsync2(0x00FE, 0x0002, lambda_1B09)

    OP_8F(0x00FE, 107070, 500, -6800, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 13)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1B3A')
    def lambda_1B3A():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_1B3A')

    DispatchAsync2(0x00FE, 0x0002, lambda_1B3A)

    Return()

# id: 0x000C offset: 0x1B48
@scena.Code('func_0C_1B48')
def func_0C_1B48():
    Sleep(300)

    SetChrPos(0x00FE, 119000, 500, -9000, 270)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrChipByIndex(0x00FE, 24)

    @scena.Lambda('lambda_1B73')
    def lambda_1B73():
        OP_99(0x00FE, 0x00, 0x07, 0x000009C4)
        Yield()

        Jump('lambda_1B73')

    DispatchAsync2(0x00FE, 0x0002, lambda_1B73)

    OP_8F(0x00FE, 106950, 500, -9000, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 13)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_1BA4')
    def lambda_1BA4():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_1BA4')

    DispatchAsync2(0x00FE, 0x0002, lambda_1BA4)

    TerminateThread(0x0009, 0x03)

    Return()

# id: 0x000D offset: 0x1BB6
@scena.Code('func_0D_1BB6')
def func_0D_1BB6():
    Sleep(1000)

    OP_8E(0x00FE, 97450, 0, -7910, 6000, 0x00)
    OP_8E(0x00FE, 100780, 0, -8000, 6000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000E offset: 0x1BEB
@scena.Code('func_0E_1BEB')
def func_0E_1BEB():
    Sleep(500)

    OP_8E(0x00FE, 97820, 0, -4690, 6000, 0x00)
    OP_8E(0x00FE, 100040, 0, -5850, 6000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000F offset: 0x1C20
@scena.Code('func_0F_1C20')
def func_0F_1C20():
    Sleep(1300)

    OP_8E(0x00FE, 96590, 10, -7800, 6000, 0x00)
    OP_8E(0x00FE, 99070, 0, -7870, 6000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0010 offset: 0x1C55
@scena.Code('func_10_1C55')
def func_10_1C55():
    FadeOut(0, 0, -1)
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
        (0x00000000, 'loc_1CCF'),
        (0x00000001, 'loc_1CD5'),
        (-1, 'loc_1CDB'),
    )

    def _loc_1CCF(): pass

    label('loc_1CCF')

    OP_A2(0x1200)

    Jump('loc_1CDB')

    def _loc_1CD5(): pass

    label('loc_1CD5')

    OP_A2(0x1201)

    Jump('loc_1CDB')

    def _loc_1CDB(): pass

    label('loc_1CDB')

    Return()

# id: 0x0011 offset: 0x1CDC
@scena.Code('func_11_1CDC')
def func_11_1CDC():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
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
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
