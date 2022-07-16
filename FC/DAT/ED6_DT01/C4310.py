import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4310   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4310.x'
    header.mapIndex       = 1
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x11AA
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
        ('ED6_DT09/CH11090._CH', 'ED6_DT09/CH11090P._CP'),
        ('ED6_DT09/CH11091._CH', 'ED6_DT09/CH11091P._CP'),
        ('ED6_DT09/CH11100._CH', 'ED6_DT09/CH11100P._CP'),
        ('ED6_DT09/CH11101._CH', 'ED6_DT09/CH11101P._CP'),
        ('ED6_DT09/CH10920._CH', 'ED6_DT09/CH10920P._CP'),
        ('ED6_DT09/CH10921._CH', 'ED6_DT09/CH10921P._CP'),
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH10950._CH', 'ED6_DT09/CH10950P._CP'),
        ('ED6_DT09/CH10951._CH', 'ED6_DT09/CH10951P._CP'),
        ('ED6_DT09/CH10990._CH', 'ED6_DT09/CH10990P._CP'),
        ('ED6_DT09/CH10991._CH', 'ED6_DT09/CH10991P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -201120,
            z           = 0,
            y           = -162390,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -112960,
            z           = 0,
            y           = -242130,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0292,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x182
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -201000,
            y           = -1000,
            z           = -86000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 40890,
            triggerZ            = 0,
            triggerY            = -264350,
            triggerRange        = 1000,
            actorX              = 40980,
            actorZ              = 0,
            actorY              = -263640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -31240,
            triggerZ            = 0,
            triggerY            = -394340,
            triggerRange        = 1000,
            actorX              = -31150,
            actorZ              = 0,
            actorY              = -395080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -273090,
            triggerZ            = 0,
            triggerY            = -231510,
            triggerRange        = 1000,
            actorX              = -272960,
            actorZ              = 0,
            actorY              = -230820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -198990,
            triggerZ            = 0,
            triggerY            = -287980,
            triggerRange        = 1000,
            actorX              = -199140,
            actorZ              = 0,
            actorY              = -288780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -151070,
            triggerZ            = 0,
            triggerY            = -263420,
            triggerRange        = 1000,
            actorX              = -151090,
            actorZ              = 0,
            actorY              = -262790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -33050,
            triggerZ            = 0,
            triggerY            = -271460,
            triggerRange        = 1000,
            actorX              = -33050,
            actorZ              = 0,
            actorY              = -270780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 110870,
            triggerZ            = 0,
            triggerY            = -327410,
            triggerRange        = 1000,
            actorX              = 111060,
            actorZ              = 0,
            actorY              = -326790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 81310,
            triggerZ            = 0,
            triggerY            = -385050,
            triggerRange        = 1000,
            actorX              = 81950,
            actorZ              = 0,
            actorY              = -385040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31260,
            triggerZ            = 0,
            triggerY            = -385140,
            triggerRange        = 1000,
            actorX              = 31920,
            actorZ              = 0,
            actorY              = -385090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2E6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2F4',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0004)

    def _loc_2F4(): pass

    label('loc_2F4')

    Return()

# id: 0x0001 offset: 0x2F5
@scena.Code('Init')
def Init():
    OP_10(0x21, 0x00)
    OP_72(0x0000, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 5, 0x69D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30F',
    )

    OP_6F(0x0005, 0)

    Jump('loc_316')

    def _loc_30F(): pass

    label('loc_30F')

    OP_6F(0x0005, 60)

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 7, 0x69F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_328',
    )

    OP_6F(0x0009, 0)

    Jump('loc_32F')

    def _loc_328(): pass

    label('loc_328')

    OP_6F(0x0009, 60)

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 1, 0x6A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_341',
    )

    OP_6F(0x0001, 0)

    Jump('loc_348')

    def _loc_341(): pass

    label('loc_341')

    OP_6F(0x0001, 60)

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 2, 0x6A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_6F(0x0002, 0)

    Jump('loc_361')

    def _loc_35A(): pass

    label('loc_35A')

    OP_6F(0x0002, 60)

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 3, 0x6A3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_373',
    )

    OP_6F(0x0003, 0)

    Jump('loc_37A')

    def _loc_373(): pass

    label('loc_373')

    OP_6F(0x0003, 60)

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 4, 0x6A4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38C',
    )

    OP_6F(0x0004, 0)

    Jump('loc_393')

    def _loc_38C(): pass

    label('loc_38C')

    OP_6F(0x0004, 60)

    def _loc_393(): pass

    label('loc_393')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 5, 0x6A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A5',
    )

    OP_6F(0x0006, 0)

    Jump('loc_3AC')

    def _loc_3A5(): pass

    label('loc_3A5')

    OP_6F(0x0006, 60)

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 6, 0x6A6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BE',
    )

    OP_6F(0x0007, 0)

    Jump('loc_3C5')

    def _loc_3BE(): pass

    label('loc_3BE')

    OP_6F(0x0007, 60)

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 7, 0x6A7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D7',
    )

    OP_6F(0x0008, 0)

    Jump('loc_3DE')

    def _loc_3D7(): pass

    label('loc_3D7')

    OP_6F(0x0008, 60)

    def _loc_3DE(): pass

    label('loc_3DE')

    Return()

# id: 0x0002 offset: 0x3DF
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3F4(): pass

    label('loc_3F4')

    Return()

# id: 0x0003 offset: 0x3F5
@scena.Code('func_03_3F5')
def func_03_3F5():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -200200, 20000, -86800, 0)
    OP_89(0x0001, -201800, 20000, -86800, 0)
    OP_89(0x0002, -201800, 20000, -85200, 0)
    OP_89(0x0003, -200200, 20000, -85200, 0)
    CameraMove(-201000, 0, -86000, 1500)
    Sleep(100)

    OP_B0(0x0000, 0x5A)
    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 1600)
    OP_70(0x0000, 1000)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/C4308._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x484
@scena.Code('func_04_484')
def func_04_484():
    EventBegin(0x00)
    OP_13(0x00E1)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xE1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0000, 1300)
    OP_70(0x0000, 1600)
    Yield()
    OP_89(0x0000, -200200, 20000, -86800, 0)
    OP_89(0x0001, -201800, 20000, -86800, 0)
    OP_89(0x0002, -201800, 20000, -85200, 0)
    OP_89(0x0003, -200200, 20000, -85200, 0)
    CameraMove(-201000, 0, -86000, 0)
    OP_73(0x0000)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -201020, 0, -89200, 180)
    OP_89(0x0001, -201020, 0, -89200, 180)
    OP_89(0x0002, -201020, 0, -89200, 180)
    OP_89(0x0003, -201020, 0, -89200, 180)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x54A
@scena.Code('func_05_54A')
def func_05_54A():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 5, 0x69D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 6, 0x69E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62A',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, 40980, 1500, -263640, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0599')
    def lambda_0599():
        ChrMoveTo(0x00FE, 40980, 1000, -263640, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0599)

    @scena.Lambda('lambda_05B4')
    def lambda_05B4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05B4)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机械人形出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000312, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_605'),
        (0x00000002, 'loc_617'),
        (0x00000001, 'loc_627'),
        (-1, 'loc_62A'),
    )

    def _loc_605(): pass

    label('loc_605')

    SetScenaFlags(ScenaFlag(0x00D3, 6, 0x69E))
    OP_6F(0x0005, 60)
    Sleep(500)

    Jump('loc_62A')

    def _loc_617(): pass

    label('loc_617')

    OP_6F(0x0005, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_627(): pass

    label('loc_627')

    OP_B4(0x00)

    Return()

    def _loc_62A(): pass

    label('loc_62A')

    If(
        (
            (Expr.Eval, "AddItem(0x000A, 1)"),
            Expr.Return,
        ),
        'loc_67E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '光弧棍',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D3, 5, 0x69D))

    Jump('loc_6EF')

    def _loc_67E(): pass

    label('loc_67E')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '光弧棍',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '光弧棍',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_6EF(): pass

    label('loc_6EF')

    Jump('loc_728')

    def _loc_6F2(): pass

    label('loc_6F2')

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
    WaitEffect(0x0F, 0x69)
    def _loc_728(): pass

    label('loc_728')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x736
@scena.Code('func_06_736')
def func_06_736():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D3, 7, 0x69F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 0, 0x6A0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_816',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    SetChrPos(0x0009, -31150, 1500, -395080, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_0785')
    def lambda_0785():
        ChrMoveTo(0x00FE, -31150, 1000, -395080, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0785)

    @scena.Lambda('lambda_07A0')
    def lambda_07A0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_07A0)

    ClearChrFlags(0x0009, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机械人形出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000313, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_7F1'),
        (0x00000002, 'loc_803'),
        (0x00000001, 'loc_813'),
        (-1, 'loc_816'),
    )

    def _loc_7F1(): pass

    label('loc_7F1')

    SetScenaFlags(ScenaFlag(0x00D4, 0, 0x6A0))
    OP_6F(0x0009, 60)
    Sleep(500)

    Jump('loc_816')

    def _loc_803(): pass

    label('loc_803')

    OP_6F(0x0009, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_813(): pass

    label('loc_813')

    OP_B4(0x00)

    Return()

    def _loc_816(): pass

    label('loc_816')

    If(
        (
            (Expr.Eval, "AddItem(0x00FD, 1)"),
            Expr.Return,
        ),
        'loc_870',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '皇家骑士铠甲',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D3, 7, 0x69F))

    Jump('loc_8ED')

    def _loc_870(): pass

    label('loc_870')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '皇家骑士铠甲',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '皇家骑士铠甲',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)

    def _loc_8ED(): pass

    label('loc_8ED')

    Jump('loc_926')

    def _loc_8F0(): pass

    label('loc_8F0')

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
    WaitEffect(0x0F, 0x6A)
    def _loc_926(): pass

    label('loc_926')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x934
@scena.Code('func_07_934')
def func_07_934():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 1, 0x6A1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A24',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_9AA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D4, 1, 0x6A1))

    Jump('loc_A21')

    def _loc_9AA(): pass

    label('loc_9AA')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
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

    def _loc_A21(): pass

    label('loc_A21')

    Jump('loc_A5A')

    def _loc_A24(): pass

    label('loc_A24')

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
    WaitEffect(0x0F, 0x6B)
    def _loc_A5A(): pass

    label('loc_A5A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xA68
@scena.Code('func_08_A68')
def func_08_A68():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 2, 0x6A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B58',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_ADE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D4, 2, 0x6A2))

    Jump('loc_B55')

    def _loc_ADE(): pass

    label('loc_ADE')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_B55(): pass

    label('loc_B55')

    Jump('loc_B8E')

    def _loc_B58(): pass

    label('loc_B58')

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
    WaitEffect(0x0F, 0x6C)
    def _loc_B8E(): pass

    label('loc_B8E')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xB9C
@scena.Code('func_09_B9C')
def func_09_B9C():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 3, 0x6A3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C8C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_C12',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D4, 3, 0x6A3))

    Jump('loc_C89')

    def _loc_C12(): pass

    label('loc_C12')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_C89(): pass

    label('loc_C89')

    Jump('loc_CC2')

    def _loc_C8C(): pass

    label('loc_C8C')

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
    WaitEffect(0x0F, 0x6D)
    def _loc_CC2(): pass

    label('loc_CC2')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xCD0
@scena.Code('func_0A_CD0')
def func_0A_CD0():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 4, 0x6A4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_D46',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D4, 4, 0x6A4))

    Jump('loc_DBD')

    def _loc_D46(): pass

    label('loc_D46')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '全回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_DBD(): pass

    label('loc_DBD')

    Jump('loc_DF6')

    def _loc_DC0(): pass

    label('loc_DC0')

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
    WaitEffect(0x0F, 0x6E)
    def _loc_DF6(): pass

    label('loc_DF6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0xE04
@scena.Code('func_0B_E04')
def func_0B_E04():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 5, 0x6A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EEE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FD, 1)"),
            Expr.Return,
        ),
        'loc_E78',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D4, 5, 0x6A5))

    Jump('loc_EEB')

    def _loc_E78(): pass

    label('loc_E78')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_EEB(): pass

    label('loc_EEB')

    Jump('loc_F24')

    def _loc_EEE(): pass

    label('loc_EEE')

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
    WaitEffect(0x0F, 0x6F)
    def _loc_F24(): pass

    label('loc_F24')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000C offset: 0xF32
@scena.Code('func_0C_F32')
def func_0C_F32():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 6, 0x6A6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_101C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FD, 1)"),
            Expr.Return,
        ),
        'loc_FA6',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D4, 6, 0x6A6))

    Jump('loc_1019')

    def _loc_FA6(): pass

    label('loc_FA6')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_1019(): pass

    label('loc_1019')

    Jump('loc_1052')

    def _loc_101C(): pass

    label('loc_101C')

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
    WaitEffect(0x0F, 0x70)
    def _loc_1052(): pass

    label('loc_1052')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000D offset: 0x1060
@scena.Code('func_0D_1060')
def func_0D_1060():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D4, 7, 0x6A7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_114A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FD, 1)"),
            Expr.Return,
        ),
        'loc_10D4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D4, 7, 0x6A7))

    Jump('loc_1147')

    def _loc_10D4(): pass

    label('loc_10D4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_1147(): pass

    label('loc_1147')

    Jump('loc_1180')

    def _loc_114A(): pass

    label('loc_114A')

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
    WaitEffect(0x0F, 0x71)
    def _loc_1180(): pass

    label('loc_1180')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
