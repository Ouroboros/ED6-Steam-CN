import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4230_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4230   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4230.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH00000._CH', 'ED6_DT07/CH00000P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
        ('ED6_DT07/CH00500._CH', 'ED6_DT07/CH00500P._CP'),
        ('ED6_DT07/CH00501._CH', 'ED6_DT07/CH00501P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT06/CH20089._CH', 'ED6_DT06/CH20089P._CP'),
    ]

# id: 0x10001 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾莉茜雅女王',
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
            name                = '杜南公爵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
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
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '茜亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x25A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x25A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 1980,
            y           = -1000,
            z           = -1550,
            range       = -2230,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFF056,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10004 offset: 0x27A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x27A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_288',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_06_69F)

    def _loc_288(): pass

    label('loc_288')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_294'),
        (-1, 'loc_2B5'),
    )

    def _loc_294(): pass

    label('loc_294')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 5, 0x665)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 4, 0x664)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(0, func_08_3803)

    def _loc_2B2(): pass

    label('loc_2B2')

    Jump('loc_2B5')

    def _loc_2B5(): pass

    label('loc_2B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_2DA',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)

    Jump('loc_2E9')

    def _loc_2DA(): pass

    label('loc_2DA')

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 3)
    ChrSetChipByIndex(0x0138, 4)

    def _loc_2E9(): pass

    label('loc_2E9')

    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_302',
    )

    Jump('loc_34E')

    def _loc_302(): pass

    label('loc_302')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_329',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -53080, 0, 12340, 3)
    CreateThread(0x000F, 0x00, 0x00, func_02_4A6)

    Jump('loc_34E')

    def _loc_329(): pass

    label('loc_329')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_333',
    )

    Jump('loc_34E')

    def _loc_333(): pass

    label('loc_333')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_33D',
    )

    Jump('loc_34E')

    def _loc_33D(): pass

    label('loc_33D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_347',
    )

    Jump('loc_34E')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_34E',
    )

    def _loc_34E(): pass

    label('loc_34E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_358',
    )

    Jump('loc_470')

    def _loc_358(): pass

    label('loc_358')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_419',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0009, -52830, 0, 7650, 179)
    ChrSetPos(0x000A, -53810, 0, 7520, 79)
    ChrSetPos(0x000B, -5180, 0, 11510, 90)
    ChrSetPos(0x000D, -3130, 0, 13730, 262)
    ChrSetPos(0x000E, -5030, 0, 13030, 135)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 5, 0x665)),
            Expr.Return,
        ),
        'loc_416',
    )

    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrSetFlags(0x000B, 0x0800)
    ChrSetFlags(0x000D, 0x0800)
    ChrSetFlags(0x000E, 0x0800)
    ChrSetChipByIndex(0x000B, 20)
    ChrSetChipByIndex(0x000D, 20)
    ChrSetChipByIndex(0x000E, 20)
    ChrSetFlags(0x0009, 0x0020)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 21)

    def _loc_416(): pass

    label('loc_416')

    Jump('loc_470')

    def _loc_419(): pass

    label('loc_419')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_423',
    )

    Jump('loc_470')

    def _loc_423(): pass

    label('loc_423')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_42D',
    )

    Jump('loc_470')

    def _loc_42D(): pass

    label('loc_42D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_437',
    )

    Jump('loc_470')

    def _loc_437(): pass

    label('loc_437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_441',
    )

    Jump('loc_470')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_44B',
    )

    Jump('loc_470')

    def _loc_44B(): pass

    label('loc_44B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_455',
    )

    Jump('loc_470')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_45F',
    )

    Jump('loc_470')

    def _loc_45F(): pass

    label('loc_45F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_469',
    )

    Jump('loc_470')

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_470',
    )

    def _loc_470(): pass

    label('loc_470')

    Return()

# id: 0x0001 offset: 0x471
@scena.Code('func_01_471')
def func_01_471():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_486',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_486(): pass

    label('loc_486')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_497',
    )

    OP_1B(0x02, 0x00, 0x0007)

    def _loc_497(): pass

    label('loc_497')

    OP_1B(0x05, 0x00, 0x000A)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x4A6
@scena.Code('func_02_4A6')
def func_02_4A6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4BB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4A6')

    def _loc_4BB(): pass

    label('loc_4BB')

    Return()

# id: 0x0003 offset: 0x4BC
@scena.Code('func_03_4BC')
def func_03_4BC():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '杜南公爵晕过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x4FB
@scena.Code('func_04_4FB')
def func_04_4FB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000A,
        (
            '#0660131281V#720F公主殿下，还有各位，\n',
            '十分感谢你们的宽宏大量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131282V我代表殿下向你们谢罪，\n',
            '对于此恩此德，没齿难忘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x583
@scena.Code('func_05_583')
def func_05_583():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_590',
    )

    Jump('loc_69B')

    def _loc_590(): pass

    label('loc_590')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_676',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5EF',
    )

    ChrTalk(
        0x00FE,
        (
            '公主殿下她\n',
            '刚才悄悄地到街上去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说是因为\n',
            '她的同学也到王都来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_673')

    def _loc_5EF(): pass

    label('loc_5EF')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '因为公主殿下回来了，\n',
            '我要把这个房间打扫一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公主殿下她\n',
            '刚才悄悄地到街上去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说是因为\n',
            '她的同学也到王都来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_673(): pass

    label('loc_673')

    Jump('loc_69B')

    def _loc_676(): pass

    label('loc_676')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_680',
    )

    Jump('loc_69B')

    def _loc_680(): pass

    label('loc_680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_68A',
    )

    Jump('loc_69B')

    def _loc_68A(): pass

    label('loc_68A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_694',
    )

    Jump('loc_69B')

    def _loc_694(): pass

    label('loc_694')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_69B',
    )

    def _loc_69B(): pass

    label('loc_69B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x69F
@scena.Code('func_06_69F')
def func_06_69F():
    EventBegin(0x00)
    CameraMove(-460, 0, 2620, 0)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0138, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0138, 255, 255, 255, 0, 0)
    ChrSetPos(0x0101, 10, 0, -5370, 225)
    ChrSetPos(0x0102, 10, 0, -5370, 225)
    ChrSetPos(0x0138, 10, 0, -5370, 225)

    @scena.Lambda('lambda_071B')
    def lambda_071B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0138, 0x0002, lambda_071B)

    @scena.Lambda('lambda_072D')
    def lambda_072D():
        ChrWalkTo(0x00FE, -90, 0, 1380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_072D)

    Sleep(500)

    @scena.Lambda('lambda_074D')
    def lambda_074D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_074D)

    @scena.Lambda('lambda_075F')
    def lambda_075F():
        ChrWalkTo(0x00FE, -1040, 0, -420, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_075F)

    Sleep(500)

    @scena.Lambda('lambda_077F')
    def lambda_077F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_077F)

    @scena.Lambda('lambda_0791')
    def lambda_0791():
        ChrWalkTo(0x00FE, 750, 0, -420, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0791)

    WaitForThreadExit(0x0138, 0x0001)
    ChrSetDirection(0x0138, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#000F呼～刚才好紧张。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '谢谢您，希尔丹夫人，\n',
            '多亏您的及时相助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很高明的手腕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650860014V#710F多谢你们的夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么……怎么样，\n',
            '在和陛下见面之前先换衣服吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121078V不用特别在意的，\n',
            '我先带你们去换吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F其实我们只要到了这里就可以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F请务必要带我们去换衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    CameraMove(-52690, 0, 7170, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetPos(0x0101, -51850, 0, 7470, 270)
    ChrSetPos(0x0102, -53280, 0, 7850, 180)
    ChrSetPos(0x0138, -52990, 0, 5970, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#000F你还真是的，\n',
            '那么害羞干嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121082V刚才那样不就很好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这可关系到我的信誉啊，\n',
            '刚才那样是绝对不行的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，希尔丹夫人，\n',
            '这个房间莫非是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F嗯……\n',
            '就是科洛蒂亚公主的房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121086V不过她一般不在\n',
            '王城里面居住，\n',
            '所以就没有怎么用过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#000F咦～是这样的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，不是说公主殿下\n',
            '在照顾着陛下的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那果然也是假消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F详细情况你们\n',
            '就直接询问陛下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860015V在女王宫二楼的就是\n',
            '艾莉茜雅女王的房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121093V我们这就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 3)
    ChrSetChipByIndex(0x0138, 4)

    Return()

# id: 0x0007 offset: 0xB74
@scena.Code('func_07_B74')
def func_07_B74():
    EventBegin(0x00)
    Fade(1000)
    SetScenaFlags(ScenaFlag(0x00C8, 4, 0x644))
    OP_28(0x004A, 0x01, 0x0100)
    OP_28(0x004A, 0x01, 0x0200)
    ChrSetChipByIndex(0x0138, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetPos(0x0138, -950, 8000, 35250, 0)
    ChrSetPos(0x0101, -2110, 8000, 34000, 0)
    ChrSetPos(0x0102, -270, 8000, 34020, 0)
    ChrSetPos(0x0008, -980, 8000, 38840, 0)
    CameraMove(-570, 8000, 34880, 2000)

    ChrTalk(
        0x0138,
        (
            '#710F陛下，打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121096V我照之前所说的把\n',
            '艾丝蒂尔和约修亚\n',
            '带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请进来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0138, -2170, 8000, 35250, 2000, 0x00)
    ChrSetDirection(0x0138, 180, 400)

    ChrTalk(
        0x0138,
        (
            '#710F我就在这里等着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121101V那么你们俩就进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F好、好的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F打扰了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    CameraMove(-100970, 0, 4310, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -100980, 0, 20410, 0)
    ChrSetPos(0x0101, -101650, 0, 3570, 0)
    ChrSetPos(0x0102, -100450, 0, 3560, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010120381V#000F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D7F')
    def lambda_0D7F():
        CameraMove(-100940, 0, 19690, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D7F)

    @scena.Lambda('lambda_0D97')
    def lambda_0D97():
        OP_6C(12000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0D97)

    @scena.Lambda('lambda_0DA7')
    def lambda_0DA7():
        OP_67(0, 4200, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0DA7)

    @scena.Lambda('lambda_0DBF')
    def lambda_0DBF():
        OP_6E(317, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0DBF)

    Sleep(6000)

    @scena.Lambda('lambda_0DD4')
    def lambda_0DD4():
        ChrWalkTo(0x00FE, -101570, 0, 14780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DD4)

    @scena.Lambda('lambda_0DEF')
    def lambda_0DEF():
        ChrWalkTo(0x00FE, -99970, 0, 15040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0DEF)

    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#0631160006V#090F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    ChrSetDirection(0x0008, 180, 300)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#090F呵呵……\n',
            '欢迎你们的到来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我的名字叫做\n',
            '艾莉茜雅·冯·奥赛雷丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121107V利贝尔王国，第２６代国王。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我、我是……\n',
            '我是艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121109V游击士协会的准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F同样是准游击士\n',
            '名叫约修亚·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121111V初次见面，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F艾丝蒂尔和约修亚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121113V能和你们两位见面，\n',
            '我真的很高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121114V没有什么好东西款待你们，\n',
            '一些茶水微表敬意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你们就收下，\n',
            '我们到那边去慢慢谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    CameraMove(-106830, 640, 12020, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(240, 0)
    ChrSetPos(0x0008, -106730, 0, 13420, 180)
    ChrSetPos(0x0101, -107390, 0, 10600, 0)
    ChrSetPos(0x0102, -106200, 0, 10610, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#090F这样啊……\n',
            '拉赛尔博士竟会卷入这样的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160007V将一切导力现象停止的\n',
            '漆黑导力器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121118V那样的物品竟然\n',
            '落入了上校手中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F博士说女王陛下\n',
            '也许可以知道理查德上校\n',
            '拿它来做什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121120V请问……有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只有一个线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121123V不过，我想上校\n',
            '应该不会知道那一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121124V我是不是有些过于担心\n',
            '了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那个……\n',
            '那个线索是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F……对你们说\n',
            '这些话是没有关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160008V数十年前，在这个王都的地下\n',
            '检测出了巨大的导力反应。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121128V当时做这项调查的\n',
            '就是中央工房的拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F巨大的导力反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F所谓王都的地下，\n',
            '就是地下水路周边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F不是的，是从比地下水路还要\n',
            '深很多的地方检测出来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121132V博士认为那是至今还没有\n',
            '失去机能的古代文明遗物\n',
            '的埋藏之地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F古代文明的遗物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F就是被称为『古代遗物』\n',
            '的古代导力器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121135V其中大部分都如塔顶的装置\n',
            '那样失去了机能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121136V另一部分稀少的，就像戴尔蒙市长的\n',
            '传家宝那样，还继续保持着机能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那样的东西在王都地下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，这么说\n',
            '那个『黑色导力器』就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F作为将埋藏的遗物的机能\n',
            '停止来使用的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121140V这种可能性是有的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121142V可是，那个遗物究竟是什么，\n',
            '为何会埋藏在那里，\n',
            '这些都还不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121143V拉赛尔博士的调查本身\n',
            '也还在非正式的进行当中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121144V如果说上校从某个地方得知了其存在，\n',
            '我认为这也并不是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121146V不管怎样，不好的事情\n',
            '有可能会因此而导致。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真是的，稍微想开一点，\n',
            '不要把事情想的那么严峻嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且只要人们陷入了困境，\n',
            '游击士就自然会出现的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121149V无论如何也会阻止上校的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121150V#090F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121151V不愧是……\n',
            '卡西乌斯阁下的孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F陛下和父亲\n',
            '以前曾经认识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121154V#090F他是我去世的孩子的朋友，\n',
            '也是拯救王国的英雄呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121155V他辞退了军衔作为游击士时，\n',
            '还时常帮我办事，承蒙他的关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是、是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这我们以前并不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121158V#090F呵呵，以他的性格来看，\n',
            '你们不知道也是比较正常的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121159V如果１０年前的战争\n',
            '没有他的奋力拼搏……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121160V这个地方还会存在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……\n',
            '详细的情况我还是不太清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F其实，这就是我的\n',
            '目的所在……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121164V你们愿意稍微听一听我这个\n',
            '上了年纪的人讲过去的故事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……好的，那是当然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121166V#010F洗耳恭听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0631160009V#090F这是１０年前的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160010V埃雷波尼亚帝国的南部\n',
            '发生了一起沉痛的事件，\n',
            '有一个小村落被全灭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160011V不是自然灾害或是魔兽的侵害，\n',
            '而是人为的屠杀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160012V然后，因为领土紧邻，\n',
            '帝国政府断定是王国军所为，\n',
            '于是向利贝尔宣战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT04/C_VIS008._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#090F帝国军在宣战的同时，\n',
            '集中大量兵力攻破了哈肯大门……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160013V利贝尔除了王都以外的地方\n',
            '转瞬之间全都被占领了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且入侵的兵力是\n',
            '王国军的３倍以上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160014V因为王国有屠杀农民的嫌疑，\n',
            '大陆诸国都采取了旁观的态度……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121176V王都要被占领也\n',
            '只是时间的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS009._CH', 0x0000, 0x0000, 0x00000064)

    ChrTalk(
        0x0008,
        (
            '#090F可是开战的两个月之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '谁都无法想象的状况\n',
            '使战局产生了巨大改变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160015V当时才开发完毕的警备飞艇\n',
            '将连接各地的关所一一夺回，\n',
            '切断了帝国军的联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160016V接着，从雷斯顿要塞开始，\n',
            '王国军总兵力乘坐水上艇出击，\n',
            '将各个地方夺了回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '蔡斯、卢安、柏斯、洛连特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121182V切断了占领各地的帝国军师团\n',
            '的补给来源后，将其各个击破。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS010._CH', 0x0000, 0x0000, 0x00000064)

    ChrTalk(
        0x0008,
        (
            '#090F制定这次反攻作战计划的就是\n',
            '卡西乌斯·布莱特上校——',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '摩尔根将军的得力助手，\n',
            '理查德上校的顶头上司，\n',
            '也就是你们的父亲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '此后不久，在游击士协会\n',
            '以及七耀教会的仲裁下，\n',
            '战争终于迎来的结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121186V可是就在那时，卡西乌斯阁下\n',
            '失去了对于他来说最重要的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS011._CH', 0x0000, 0x0000, 0x00000064)

    ChrTalk(
        0x0008,
        (
            '#090F那就是莱娜·布莱特女士……\n',
            '艾丝蒂尔的母亲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160017V洛连特的钟楼，在反攻作战时\n',
            '被走投无路的帝国军师团\n',
            '恶意报复而破坏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而那时……\n',
            '后面的你们都知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121190V卡西乌斯阁下，甚至连\n',
            '夫人最后的一眼都没有见到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AE(0x000001F4)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#000F……怎么会……………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121192V怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F……自己确立的作战计划，\n',
            '结果却导致了夫人的死去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121194V因此而深深自责的卡西乌斯阁下\n',
            '辞去了军衔，走上了游击士的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121195V守护在幸存下来的你的身边……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121196V这样做是为了用自己的双手\n',
            '来保护心爱的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F笨蛋……爸爸……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121198V因为爸爸的过失而导致\n',
            '妈妈的离去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121199V不是这样的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121202V这一切都是没有实力来\n',
            '保护自己子民的女王的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，艾丝蒂尔。\n',
            '我没有保护好你的妈妈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121204V对于此事……\n',
            '请接受我深深的歉意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F没、没有必要道歉的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '女王陛下一直守护着\n',
            '这来之不易的和平……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121207V爸爸他们拼死守护着\n',
            '这个国家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121208V妈妈换来的生命\n',
            '由我来守护……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样就可以了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121210V#090F艾丝蒂尔……\n',
            '谢谢，你是个优秀的孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '能够见到你们\n',
            '真是太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121212V我发自心底的这么认为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F女王陛下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F不过，正因为如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '正因为如此，我不希望\n',
            '你们遇到任何危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121220V在卡西乌斯阁下外出的时候，\n',
            '你们俩万一出了什么事情，\n',
            '让我怎么交待……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160018V因此，请你们回到洛连特的家中\n',
            '等待你们的父亲回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F可、可是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F可是，女王陛下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '由父亲卡西乌斯取回的、\n',
            '陛下您一直守护着的和平，\n',
            '现在即将开始动摇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F因为『黑色导力器』所带来的事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就这样下去，上校一旦达成\n',
            '让公爵大人成为国王的目的时，\n',
            '现在的和平会变成什么样的呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121228V请您务必要考虑一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F对、对不起，女王陛下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121231V我们两个自从成为游击士以来，\n',
            '就作为爸爸的代理完成任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121232V从那时开始，空贼事件，\n',
            '传递信件，打开奇怪的小包裹，\n',
            '就这样在各地游历……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121233V感觉就好像是被爸爸背着\n',
            '来到这里的一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所以……我也想要守护着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121235V这和平的、幸福的每一天……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121236V以及这一路上所认识的，\n',
            '关心我、喜欢我的人们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '女王殿下也好，像我的妈妈那样的人\n',
            '也好，我会用自己的方法来守护着的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121240V的确……\n',
            '和那个孩子所说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121242V#090F我也终于明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121243V我想通过艾丝蒂尔你们\n',
            '向游击士协会委托\n',
            '一些需要解决的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F女王陛下……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121245V#010F陛下……\n',
            '请您尽管吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F委托的内容就是：将被情报部\n',
            '囚禁的人们救出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121247V其中还包含我的孙女\n',
            '科洛蒂娅公主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，公主殿下果然\n',
            '被抓到某个地方去了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121250V回想起来，这次的政变是\n',
            '因为我要推选那个孩子\n',
            '作为新一代国王而开始的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不是杜南公爵对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F嗯，虽说他是我的\n',
            '外甥，但杜南公爵\n',
            '是个问题多多的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121253V相比之下，虽说不算很成熟，\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121254V在考虑了王国的未来之后……\n',
            '我做出的决定就是\n',
            '选择科洛蒂娅公主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，公主的事情\n',
            '我不是很了解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121256V不过不管怎么说，做出\n',
            '这样的决定应该是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0631160019V#090F呵呵，可是无论何时，这个世界\n',
            '总是倾向于对女性当权\n',
            '持反对的态度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121258V何况，对于被大国侵略\n',
            '的过去还记忆犹新的今天……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '连续２代都由女王来统治，\n',
            '结果只会导致国力的衰弱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121260V抱有这种想法的人物会出现，\n',
            '也没有什么不可思议的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F原来如此……\n',
            '那样的人物就是理查德上校吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121263V我想推选科洛蒂娅\n',
            '作为新一代国王的想法\n',
            '不知何时被他得知了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160020V于是他就把这件事告诉了公爵，\n',
            '然后发动了这次政变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160021V实际上是为了暗中操纵公爵，\n',
            '把利贝尔变成不弱于周边大国\n',
            '的强大军事国家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121266V#010F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121267V终于明白这次\n',
            '事件的全貌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F变成强大的军事国家……\n',
            '具体是要怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F会有各种各样的做法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121270V提高税率，\n',
            '增大军费开支……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121271V开发大量的以破坏为目的\n',
            '的导力兵器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121272V采取大规模的征兵制……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '转变成可以和利贝尔不予以认可的\n',
            '猎兵团签订合法契约……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F的确，与之类似的要求\n',
            '上校也向我提出过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说这也是出自纯粹的爱国心\n',
            '的一番话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121277V但是我无论如何\n',
            '也不认为那是正确的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121278V要守护国家，\n',
            '仅靠军事力量是不行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121279V和他国协调好关系，\n',
            '在外交上努力一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121280V加强技术交流、经济交流，\n',
            '可以让全国各地更加繁荣，\n',
            '也就可以牢固地守卫国家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……陛下所说的\n',
            '的确才是有道理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯嗯！\n',
            '不谋而合！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F但是，上校一口断定这是\n',
            '带有妇人之见的理想论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121284V而且还以科洛蒂娅的安全\n',
            '来要挟我退位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F大部分掌权者的亲人都被\n',
            '作为了人质，所以不敢违抗上校。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121287V可我是女王。\n',
            '不能因为骨肉之情而\n',
            '出卖国家的未来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话虽然这么说，但那个孩子\n',
            '是我唯一的一个孙女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121289V我不能见死不救啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F女王陛下……\n',
            '请您放心吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121291V#010F您委托的旨意，我们已经清楚的知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121292V一定会将包括公主殿下在内的\n',
            '所有人质救出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121293V#090F非常感谢……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121294V这样一来，上校的要挟\n',
            '始终都不会让我屈服的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F请、请问，\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还有『黑色导力器』那件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121297V如果现在要帮助女王陛下您逃离这里，\n',
            '我认为也不是不可能的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121298V#090F谢谢你，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121299V不过，我如果逃离了，\n',
            '也并不能改变局势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160022V而且这件事究竟与『黑色导力器』有着\n',
            '怎样的联系，对此我很在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我要向上校问清楚\n',
            '他的真实意图所在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160023V请理解我的心意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    CameraMove(-52350, 0, 6280, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0138, 0)
    ChrSetPos(0x0101, -53470, 0, 6160, 90)
    ChrSetPos(0x0102, -51450, 0, 6000, 270)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#000F哈～真是一位\n',
            '充满魅力的女性啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121303V和蔼可亲而又内心坚强，\n',
            '相当的坚毅啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '等我到了那个年纪时\n',
            '也要成为那样\n',
            '优雅的老奶奶呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F优雅……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过的确是很有一国之主\n',
            '风范的一位女性呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121308V真想这就阻止政变，\n',
            '救出女王陛下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F其实这并不属于游击士\n',
            '的管辖范围的呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121310V不过无论如何，也让我们\n',
            '尽力去完成吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还有就是从女王那里\n',
            '听说的父亲所做的事，\n',
            '简直就像是在做梦一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121313V还会有我不知道的事情\n',
            '冒出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……说不定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0138, 255, 255, 255, 0, 0)
    ChrSetPos(0x0138, -51030, 0, 420, 225)

    ChrTalk(
        0x0138,
        (
            '料理还在准备中，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121315V你们准备完毕了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3657')
    def lambda_3657():
        ChrTurnDirection(0x00FE, 0x0138, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3657)

    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121316V#000F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_368D')
    def lambda_368D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0138, 0x0002, lambda_368D)

    @scena.Lambda('lambda_369F')
    def lambda_369F():
        ChrWalkTo(0x00FE, -52060, 0, 3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_369F)

    @scena.Lambda('lambda_36BA')
    def lambda_36BA():
        ChrTurnDirection(0x00FE, 0x0138, 0)
        Yield()

        Jump('lambda_36BA')

    DispatchAsync2(0x0101, 0x0001, lambda_36BA)

    @scena.Lambda('lambda_36CB')
    def lambda_36CB():
        ChrTurnDirection(0x00FE, 0x0138, 0)
        Yield()

        Jump('lambda_36CB')

    DispatchAsync2(0x0102, 0x0001, lambda_36CB)

    Sleep(300)

    CameraMove(-52330, 0, 5310, 1000)
    WaitForThreadExit(0x0138, 0x0001)

    ChrTalk(
        0x0138,
        (
            '#0650121317V#710F那我们就立刻\n',
            '回休息室去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121318V已经１１点过了……\n',
            '再过一会就是新的一天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哇啊，已经这么晚了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F过了很长的时间呢，\n',
            '当我们在和陛下聊天时。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121321V如果在这么待下去，\n',
            '看守就会觉得可疑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    EventEnd(0x00)
    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    OP_1B(0x02, 0x00, 0xFFFF)

    Return()

# id: 0x0008 offset: 0x3803
@scena.Code('func_08_3803')
def func_08_3803():
    MapClearFlags(0x10000000)
    OP_28(0x004E, 0x01, 0x0004)
    EventBegin(0x00)
    CameraMove(1080, 0, 3170, 0)
    OP_67(0, 5080, -10000, 0)
    CameraSetDistance(2190, 0)
    OP_6C(44000, 0)
    OP_6E(426, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0009, 0, 0, 9760, 180)
    ChrSetPos(0x000B, -1480, 0, 9280, 180)
    ChrSetPos(0x000D, 0, 0, 8350, 180)
    ChrSetPos(0x000E, 1400, 0, 9310, 180)
    ChrSetPos(0x0101, -90, 0, 920, 0)
    ChrSetPos(0x0105, -1330, 0, 430, 0)
    ChrSetPos(0x0103, 930, 0, 430, 0)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetChipByIndex(0x0103, 11)
    ChrSetChipByIndex(0x0105, 13)
    FadeIn(1000, 0)
    CameraMove(1130, 0, 6000, 1000)

    ChrTalk(
        0x0009,
        (
            '#0640131195V#224F叛、叛逆者！\n',
            '居然恬不知耻地跑到这里来了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131196V明知我是将要继承王位的人，\n',
            '你们还要动粗吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131197V#509F#2P别说笑了，你那发型已经够搞笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131198V你现在已经再也不可能成为国王了，\n',
            '真正的下任国王在我们身旁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640131199V#226F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131200V#020F#2P您是杜南公爵吧。\n',
            '我们是游击士协会派来的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131201V科洛蒂娅殿下委托我们来救出女王陛下。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131202V#021F如果您能通融一下，\n',
            '那我们也不会为难您的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640131203V#222F科、科洛蒂娅！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131204V那个小姑娘……\n',
            '简直就是碍手碍脚的家伙！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131205V#043F#2P杜南王叔……\n',
            '请您不要再执迷不悟了好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131206V王叔，\n',
            '您已经被理查德上校给利用了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640131207V#223F你、你是谁啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131208V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0640131209V#222F你、你、你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0640131210V#224F#3S你不是科洛蒂娅吗！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0640131211V#226F那样的发型和装扮，像个什么样子！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131212V#007F#2P终于发觉了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131213V反应这么慢……\n',
            '怪不得你在卢安没能注意到啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131214V#027F#2P虽然我对您不是很了解，\n',
            '不过的确是个很迟钝的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131215V#542F#2P对不起，一直瞒着您这件事，\n',
            '都是我的不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640131216V#226F根、根本就是把我当傻瓜来耍！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131217V这就是为何女人这种生物\n',
            '不可信任的原因啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131218V狡猾、小气，为一些不值得的\n',
            '小事情故意找碴儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131219V怎能把王冠交给这样无聊的家伙呢！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131220V#002F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131221V#024F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131222V#043F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0640131223V#223F……嗯……不过………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000B,
        (
            '#2620131224V#5P殿、殿下……\n',
            '情况不妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2660131225V#5P还、还是投降吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    OP_63(0x0105)
    OP_63(0x0103)

    ChrTalk(
        0x0101,
        (
            '#0010131226V#001F#2P哈哈……真是没用的手下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131227V#021F#2P哎呀呀，看来我得对你另眼相看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131228V在这样的时代里，\n',
            '竟然还会有人敢做出如此臆断的发言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131229V#542F#2P对、对不起了王叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131230V#045F这回有点儿……\n',
            '我也没办法帮您求情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4129')
    def lambda_4129():
        CameraMove(420, 0, 10250, 700)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4129)

    @scena.Lambda('lambda_4141')
    def lambda_4141():
        ChrWalkTo(0x00FE, 290, 0, 22950, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4141)

    Sleep(50)

    @scena.Lambda('lambda_4161')
    def lambda_4161():
        ChrWalkTo(0x00FE, 290, 0, 22950, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4161)

    Sleep(50)

    @scena.Lambda('lambda_4181')
    def lambda_4181():
        ChrWalkTo(0x00FE, 290, 0, 22950, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4181)

    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0105, 0xFF)
    Battle(0x000003AA, 0x00000000, 0x00, 0x0002, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_41C0'),
        (-1, 'loc_41C3'),
    )

    def _loc_41C0(): pass

    label('loc_41C0')

    OP_B4(0x00)

    Return()

    def _loc_41C3(): pass

    label('loc_41C3')

    EventBegin(0x00)
    CameraMove(-2360, 0, 10280, 0)
    OP_67(0, 5270, -10000, 0)
    CameraSetDistance(3260, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x000B, -5180, 0, 11510, 90)
    ChrSetPos(0x000D, -3130, 0, 13730, 262)
    ChrSetPos(0x000E, -5030, 0, 13030, 135)
    ChrSetChipByIndex(0x000B, 20)
    ChrSetChipByIndex(0x000D, 20)
    ChrSetChipByIndex(0x000E, 20)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrSetFlags(0x000B, 0x0800)
    ChrSetFlags(0x000D, 0x0800)
    ChrSetFlags(0x000E, 0x0800)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4282',
    )

    ChrSetPos(0x0009, -4810, 0, 7920, 90)

    Jump('loc_42A8')

    def _loc_4282(): pass

    label('loc_4282')

    ChrSetPos(0x0009, -6370, 0, 7980, 90)
    ChrSetFlags(0x0009, 0x0020)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 21)

    def _loc_42A8(): pass

    label('loc_42A8')

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_42B4'),
        (-1, 'loc_4C5B'),
    )

    def _loc_42B4(): pass

    label('loc_42B4')

    ChrSetPos(0x0101, -2120, 0, 8860, 0)
    ChrSetPos(0x0105, -850, 0, 8130, 0)
    ChrSetPos(0x0103, -2400, 0, 7180, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_2B(0x004D, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010131231V#502F#2P好的，解决了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131232V#006F接下来，该轮到公爵您了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4354')
    def lambda_4354():
        CameraMove(-5080, 0, 8690, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4354)

    @scena.Lambda('lambda_436C')
    def lambda_436C():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_436C)

    Sleep(50)

    @scena.Lambda('lambda_437F')
    def lambda_437F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_437F)

    Sleep(50)

    @scena.Lambda('lambda_4392')
    def lambda_4392():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4392)

    ChrMoveTo(0x0009, -5580, 0, 7960, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0103,
        (
            '#0030131233V#027F#2P由女人手中挥出的鞭子，\n',
            '想不想品尝一下是什么滋味呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0009, -6430, 0, 7860, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0640131234V#226F哇、哇呀呀呀呀呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131235V不要过来，不要靠近我呀啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131236V#045F对不起……\n',
            '请您原谅我们吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0640131237V#222F可恶，这样的话，\n',
            '我就只好拿陛下当盾牌……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131238V#224F……嘿～哈～喝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4518')
    def lambda_4518():
        ChrSetDirection(0x00FE, 270, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4518)

    ChrMoveTo(0x0009, -8250, 0, 7900, 6000, 0x00)
    PlaySE(125, 0x00, 0x64)

    ChrTalk(
        0x0009,
        (
            '#0640131239V#228F#10A呜……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_4560')
    def lambda_4560():
        ChrSetDirection(0x00FE, 800, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4560)

    ChrJumpTo(0x0009, -7070, 0, 7980, 800, 8000)

    @scena.Lambda('lambda_4585')
    def lambda_4585():
        ChrSetDirection(0x00FE, 800, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4585)

    ChrJumpTo(0x0009, -6370, 0, 7980, 400, 8000)
    PlaySE(48, 0x00, 0x64)
    OP_62(0x0009, 0x0000012C, 1600, 0x30, 0x32, 0x00000096, 0x00)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0020)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 21)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)

    @scena.Lambda('lambda_4639')
    def lambda_4639():
        CameraMove(-5790, 0, 8440, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4639)

    @scena.Lambda('lambda_4651')
    def lambda_4651():
        ChrWalkTo(0x00FE, -5810, 0, 9310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4651)

    Sleep(200)

    @scena.Lambda('lambda_4671')
    def lambda_4671():
        ChrWalkTo(0x00FE, -4910, 0, 7300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_4671)

    Sleep(200)

    @scena.Lambda('lambda_4691')
    def lambda_4691():
        ChrWalkTo(0x00FE, -4560, 0, 8870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_4691)

    @scena.Lambda('lambda_46AC')
    def lambda_46AC():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_46AC')

    DispatchAsync2(0x0101, 0x0001, lambda_46AC)

    @scena.Lambda('lambda_46BD')
    def lambda_46BD():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_46BD')

    DispatchAsync2(0x0103, 0x0001, lambda_46BD)

    @scena.Lambda('lambda_46CE')
    def lambda_46CE():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_46CE')

    DispatchAsync2(0x0105, 0x0001, lambda_46CE)

    WaitForThreadExit(0x0101, 0x0002)
    OP_63(0x0009)

    ChrTalk(
        0x0101,
        (
            '#0010131240V#007F哎呀……\n',
            '这家伙好像受惊过度了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131241V#021F不过他确实阻碍我们了，\n',
            '这不是个很有意思的教训吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131242V#047F嗯……\n',
            '真是不幸的事件啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131243V#049F可是……难道……\n',
            '就让王叔昏迷在这里行吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -490, 0, -530, 270)
    OP_4A(0x000A, 255)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0660131244V#1P……公、公爵大人！？　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4827')
    def lambda_4827():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4827)

    @scena.Lambda('lambda_4835')
    def lambda_4835():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4835)

    @scena.Lambda('lambda_4843')
    def lambda_4843():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4843)

    @scena.Lambda('lambda_4851')
    def lambda_4851():
        ChrWalkTo(0x000A, -6340, 0, 7290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4851)

    CameraMove(-2009, 0, 6520, 1000)
    Sleep(200)

    @scena.Lambda('lambda_4882')
    def lambda_4882():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4882')

    DispatchAsync2(0x0101, 0x0001, lambda_4882)

    @scena.Lambda('lambda_4893')
    def lambda_4893():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4893')

    DispatchAsync2(0x0103, 0x0001, lambda_4893)

    @scena.Lambda('lambda_48A4')
    def lambda_48A4():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_48A4')

    DispatchAsync2(0x0105, 0x0001, lambda_48A4)

    @scena.Lambda('lambda_48B5')
    def lambda_48B5():
        CameraMove(-5850, 0, 8290, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_48B5)

    WaitForThreadExit(0x000A, 0x0001)
    ChrTurnDirection(0x000A, 0x0009, 800)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010131245V#004F啊，是菲利普先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0105, 400)

    ChrTalk(
        0x000A,
        (
            '#0660131246V#722F艾丝蒂尔小姐……\n',
            '还有科洛蒂娅公主……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131247V对于这次我家主人的执迷不悟，\n',
            '我感到非常的抱歉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131248V这一切都是因为我没有\n',
            '好好教导大人而导致的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131249V#723F因此，如果你们要惩罚的话，\n',
            '就请惩罚在下吧！　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '菲利普向艾丝蒂尔等人深深地低下了头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010131250V#004F等、等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131251V#048F菲利普先生……\n',
            '请您先抬起头来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131252V我们一行人，是为了救祖母……\n',
            '是为了营救女王陛下而赶来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131253V原本就和王叔是没有任何牵连的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131254V因此，菲利普先生……\n',
            '请把王叔送到我的房间养伤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0660131255V#721F公、公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131256V#020F事实上他没有受到什么伤害哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131257V就只是因为突然受惊而昏厥，\n',
            '过一会儿就没事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0660131258V#722F大、大家……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131259V你们的大恩大德，我决对不会忘记的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52AD')

    def _loc_4C5B(): pass

    label('loc_4C5B')

    ChrSetPos(0x0101, -5810, 0, 9310, 315)
    ChrSetPos(0x0105, -4910, 0, 7300, 336)
    ChrSetPos(0x0103, -4560, 0, 8870, 296)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    CameraMove(-5790, 0, 8440, 0)

    @scena.Lambda('lambda_4CB4')
    def lambda_4CB4():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4CB4')

    DispatchAsync2(0x0101, 0x0001, lambda_4CB4)

    @scena.Lambda('lambda_4CC5')
    def lambda_4CC5():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4CC5')

    DispatchAsync2(0x0103, 0x0001, lambda_4CC5)

    @scena.Lambda('lambda_4CD6')
    def lambda_4CD6():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4CD6')

    DispatchAsync2(0x0105, 0x0001, lambda_4CD6)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010131260V#007F呼～～\n',
            '想不到连公爵也一起打晕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131261V#020F如果可以办到的话，\n',
            '倒是只需要打倒特务兵就行了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131241V#021F不过他确实阻碍我们了，\n',
            '这不是个很有意思的教训吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131242V#047F嗯……\n',
            '真是不幸的事件啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131243V#049F可是……难道……\n',
            '就让王叔昏迷在这里行吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -490, 0, -530, 270)
    OP_4A(0x000A, 255)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0660131244V#1P……公、公爵大人！？　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4E79')
    def lambda_4E79():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4E79)

    @scena.Lambda('lambda_4E87')
    def lambda_4E87():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4E87)

    @scena.Lambda('lambda_4E95')
    def lambda_4E95():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4E95)

    @scena.Lambda('lambda_4EA3')
    def lambda_4EA3():
        ChrWalkTo(0x000A, -6340, 0, 7290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4EA3)

    CameraMove(-2009, 0, 6520, 1000)
    Sleep(200)

    @scena.Lambda('lambda_4ED4')
    def lambda_4ED4():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4ED4')

    DispatchAsync2(0x0101, 0x0001, lambda_4ED4)

    @scena.Lambda('lambda_4EE5')
    def lambda_4EE5():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4EE5')

    DispatchAsync2(0x0103, 0x0001, lambda_4EE5)

    @scena.Lambda('lambda_4EF6')
    def lambda_4EF6():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4EF6')

    DispatchAsync2(0x0105, 0x0001, lambda_4EF6)

    @scena.Lambda('lambda_4F07')
    def lambda_4F07():
        CameraMove(-5850, 0, 8290, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4F07)

    WaitForThreadExit(0x000A, 0x0001)
    ChrTurnDirection(0x000A, 0x0009, 800)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010131245V#004F啊，是菲利普先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0105, 400)

    ChrTalk(
        0x000A,
        (
            '#0660131246V#722F艾丝蒂尔小姐……\n',
            '还有科洛蒂娅公主……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131247V对于这次我家主人的执迷不悟，\n',
            '我感到非常的抱歉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131248V这一切都是因为我没有\n',
            '好好教导大人而导致的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131249V#723F因此，如果你们要惩罚的话，\n',
            '就请惩罚在下吧！　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '菲利普向艾丝蒂尔等人深深地低下了头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010131250V#004F等、等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131251V#048F菲利普先生……\n',
            '请您先抬起头来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131252V我们一行人，是为了救祖母……\n',
            '是为了营救女王陛下而赶来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131253V原本就和王叔是没有任何牵连的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131254V因此，菲利普先生……\n',
            '请把王叔送到我的房间养伤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0660131255V#721F公、公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131256V#020F事实上他没有受什么重伤哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131278V只是因为受了点打击昏过去了，\n',
            '过一会儿就没事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0660131258V#722F大、大家……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131259V你们的大恩大德，我决对不会忘记的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52AD')

    def _loc_52AD(): pass

    label('loc_52AD')

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0009, -52830, 0, 7650, 179)
    ChrSetPos(0x000A, -53810, 0, 7520, 79)
    OP_63(0x0009)
    CameraMove(-5920, 0, 8680, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    ChrSetPos(0x0101, -5920, 0, 8680, 0)
    ChrSetPos(0x0105, -5920, 0, 8680, 0)
    ChrSetPos(0x0103, -5920, 0, 8680, 0)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x00CC, 5, 0x665))
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x5368
@scena.Code('func_09_5368')
def func_09_5368():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetChipByIndex(0x0103, 11)
    ChrSetChipByIndex(0x0105, 13)
    CameraMove(-100980, 0, 8360, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -101110, 0, 3990, 0)
    ChrSetPos(0x0103, -102060, 0, 2930, 0)
    ChrSetPos(0x0105, -100330, 0, 2930, 0)
    FadeIn(2000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F一个人也没有？！（※仮）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F肯定是在里面的阳台！（※仮）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00D0, 0, 0x680))
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x546E
@scena.Code('func_0A_546E')
def func_0A_546E():
    MapClearFlags(0x02000000)
    OP_1B(0x05, 0x00, 0xFFFF)

    Return()

# id: 0x000B offset: 0x5479
@scena.Code('func_0B_5479')
def func_0B_5479():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54F0',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0138, 0x0101, 400)

    NpcTalk(
        0x0000,
        '希尔丹夫人',
        (
            '#0650121094V#710F女王陛下的房间\n',
            '就在这个女王宫的二楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_54F0(): pass

    label('loc_54F0')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
