import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1500   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1500.x'
    header.mapIndex       = 61
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/C1500._SN', 'ED6_DT01/C1500_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFE01D8,
            dword_04        = 0xFFFFFFD8,
            dword_08        = 0x0002B944,
            word_0C         = 0x0004,
            word_0E         = 0x00E1,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 260,
            word_32         = 240,
            word_34         = 300,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 61,
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
        ('ED6_DT09/CH10140._CH', 'ED6_DT09/CH10140P._CP'),
        ('ED6_DT09/CH10141._CH', 'ED6_DT09/CH10141P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00102._CH', 'ED6_DT07/CH00102P._CP'),
        ('ED6_DT09/CH10200._CH', 'ED6_DT09/CH10200P._CP'),
        ('ED6_DT09/CH10201._CH', 'ED6_DT09/CH10201P._CP'),
        ('ED6_DT09/CH10880._CH', 'ED6_DT09/CH10880P._CP'),
        ('ED6_DT09/CH10881._CH', 'ED6_DT09/CH10881P._CP'),
        ('ED6_DT09/CH11160._CH', 'ED6_DT09/CH11160P._CP'),
        ('ED6_DT09/CH11161._CH', 'ED6_DT09/CH11161P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150000,
            z                   = 7800,
            y                   = 63100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150000,
            z                   = 7800,
            y                   = 63100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150000,
            z                   = 7800,
            y                   = 63100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150000,
            z                   = 7800,
            y                   = 63100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150300,
            z                   = 6800,
            y                   = 90200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150300,
            z                   = 6800,
            y                   = 90200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150300,
            z                   = 6800,
            y                   = 90200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -150300,
            z                   = 6800,
            y                   = 90200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '照相机',
            x                   = 99000,
            z                   = 0,
            y                   = 99000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾丝蒂尔',
            x                   = 99000,
            z                   = 0,
            y                   = 99000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '约修亚',
            x                   = 99000,
            z                   = 0,
            y                   = 99000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 99000,
            z                   = 0,
            y                   = 99000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古罗尼山道·关所方向',
            x                   = -140810,
            z                   = 6010,
            y                   = -31010,
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
            name                = '西柏斯街道方向',
            x                   = -119390,
            z                   = -60,
            y                   = 180920,
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
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x312
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -146390,
            z           = 2009,
            y           = 152190,
            word_0C     = 0x0000,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -148000,
            z           = 2090,
            y           = 136280,
            word_0C     = 0x0000,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -154200,
            z           = 1990,
            y           = 120790,
            word_0C     = 0x0000,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CC,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -154710,
            z           = 4070,
            y           = 99880,
            word_0C     = 0x003A,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CC,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -154180,
            z           = 4030,
            y           = 76310,
            word_0C     = 0x0075,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -162330,
            z           = 4019,
            y           = 46020,
            word_0C     = 0x0074,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -135360,
            z           = 3950,
            y           = 20570,
            word_0C     = 0x0063,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CC,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -131150,
            z           = 2040,
            y           = 55190,
            word_0C     = 0x0039,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CC,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -151910,
            z           = 5910,
            y           = -11960,
            word_0C     = 0x0000,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x40E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -143900,
            y           = 2800,
            z           = 74200,
            range       = 2000,
            dword_10    = 0x000004B0,
            dword_14    = 0x00000000,
            dword_18    = 0x00010040,
            dword_1C    = 0x00000000,
        ),
    )

# id: 0x10004 offset: 0x42E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -123590,
            triggerZ            = 4010,
            triggerY            = 89800,
            triggerRange        = 1000,
            actorX              = -122930,
            actorZ              = 5010,
            actorY              = 89680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -128169,
            triggerZ            = 4130,
            triggerY            = 22090,
            triggerRange        = 1000,
            actorX              = -127650,
            actorZ              = 5630,
            actorY              = 22150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x476
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x477
@scena.Code('func_01_477')
def func_01_477():
    OP_16(0x02, 4000, -267000, -56000, 196670)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 2, 0x372)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49B',
    )

    OP_6F(0x0000, 0)

    Jump('loc_4A2')

    def _loc_49B(): pass

    label('loc_49B')

    OP_6F(0x0000, 60)

    def _loc_4A2(): pass

    label('loc_4A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 3, 0x373)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B4',
    )

    OP_6F(0x0001, 0)

    Jump('loc_4BB')

    def _loc_4B4(): pass

    label('loc_4B4')

    OP_6F(0x0001, 60)

    def _loc_4BB(): pass

    label('loc_4BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 3, 0x373)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_4D4')

    def _loc_4CD(): pass

    label('loc_4CD')

    OP_6F(0x0000, 60)

    def _loc_4D4(): pass

    label('loc_4D4')

    Return()

# id: 0x0002 offset: 0x4D5
@scena.Code('func_02_4D5')
def func_02_4D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4EA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4D5')

    def _loc_4EA(): pass

    label('loc_4EA')

    Return()

# id: 0x0003 offset: 0x4EB
@scena.Code('func_03_4EB')
def func_03_4EB():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 2, 0x372)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5D5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_55F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006E, 2, 0x372))

    Jump('loc_5D2')

    def _loc_55F(): pass

    label('loc_55F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_5D2(): pass

    label('loc_5D2')

    Jump('loc_60B')

    def _loc_5D5(): pass

    label('loc_5D5')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x17)
    def _loc_60B(): pass

    label('loc_60B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x619
@scena.Code('func_04_619')
def func_04_619():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 3, 0x373)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 6, 0x396)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F5',
    )

    ChrSetRGBAMask(0x0016, 255, 255, 255, 0, 0)
    ChrSetPos(0x0016, -128169, 4130, 22090, 320)
    ChrTurnDirection(0x0016, 0x0000, 0)

    @scena.Lambda('lambda_0668')
    def lambda_0668():
        ChrMoveTo(0x00FE, -128169, 4130, 22090, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_0668)

    @scena.Lambda('lambda_0683')
    def lambda_0683():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_0683)

    ChrClearFlags(0x0016, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x000000D0, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0016, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_6D0'),
        (0x00000002, 'loc_6E2'),
        (0x00000001, 'loc_6F2'),
        (-1, 'loc_6F5'),
    )

    def _loc_6D0(): pass

    label('loc_6D0')

    SetScenaFlags(ScenaFlag(0x0072, 6, 0x396))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_6F5')

    def _loc_6E2(): pass

    label('loc_6E2')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_6F2(): pass

    label('loc_6F2')

    OP_B4(0x00)

    Return()

    def _loc_6F5(): pass

    label('loc_6F5')

    If(
        (
            (Expr.Eval, "AddItem(0x0133, 1)"),
            Expr.Return,
        ),
        'loc_74B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '珍珠耳环',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006E, 3, 0x373))

    Jump('loc_7C0')

    def _loc_74B(): pass

    label('loc_74B')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '珍珠耳环',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '珍珠耳环',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_7C0(): pass

    label('loc_7C0')

    Jump('loc_7F9')

    def _loc_7C3(): pass

    label('loc_7C3')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x18)
    def _loc_7F9(): pass

    label('loc_7F9')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
