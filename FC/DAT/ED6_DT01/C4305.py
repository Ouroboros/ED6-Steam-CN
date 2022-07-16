import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4305_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4305   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4305.x'
    header.mapIndex       = 216
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xF84
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
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
        ('ED6_DT09/CH11000._CH', 'ED6_DT09/CH11000P._CP'),
        ('ED6_DT09/CH11001._CH', 'ED6_DT09/CH11001P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
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

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -160720,
            z           = 0,
            y           = 43100,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x156
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -239000,
            y           = -1000,
            z           = 42000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -376000,
            y           = -1000,
            z           = 55000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0x196
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -192730,
            triggerZ            = 0,
            triggerY            = -77230,
            triggerRange        = 1000,
            actorX              = -192000,
            actorZ              = 0,
            actorY              = -77080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -91700,
            triggerZ            = 0,
            triggerY            = 42960,
            triggerRange        = 1000,
            actorX              = -91050,
            actorZ              = 0,
            actorY              = 43060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -306370,
            triggerZ            = 0,
            triggerY            = 53900,
            triggerRange        = 1000,
            actorX              = -305690,
            actorZ              = 0,
            actorY              = 54020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -313240,
            triggerZ            = 0,
            triggerY            = -24960,
            triggerRange        = 1000,
            actorX              = -314050,
            actorZ              = 0,
            actorY              = -25090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -282740,
            triggerZ            = 0,
            triggerY            = -81200,
            triggerRange        = 1000,
            actorX              = -283050,
            actorZ              = 0,
            actorY              = -81950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -166860,
            triggerZ            = 0,
            triggerY            = -25200,
            triggerRange        = 1000,
            actorX              = -166160,
            actorZ              = 0,
            actorY              = -25090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_27C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0004)

    def _loc_27C(): pass

    label('loc_27C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_28A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0006)

    def _loc_28A(): pass

    label('loc_28A')

    Return()

# id: 0x0001 offset: 0x28B
@scena.Code('Init')
def Init():
    OP_10(0x14, 0x00)
    OP_10(0x13, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 7, 0x6BF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A3',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2AA')

    def _loc_2A3(): pass

    label('loc_2A3')

    OP_6F(0x0004, 60)

    def _loc_2AA(): pass

    label('loc_2AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 1, 0x6C1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BC',
    )

    OP_6F(0x0006, 0)

    Jump('loc_2C3')

    def _loc_2BC(): pass

    label('loc_2BC')

    OP_6F(0x0006, 60)

    def _loc_2C3(): pass

    label('loc_2C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 3, 0x6C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D5',
    )

    OP_6F(0x0007, 0)

    Jump('loc_2DC')

    def _loc_2D5(): pass

    label('loc_2D5')

    OP_6F(0x0007, 60)

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 5, 0x6C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EE',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2F5')

    def _loc_2EE(): pass

    label('loc_2EE')

    OP_6F(0x0002, 60)

    def _loc_2F5(): pass

    label('loc_2F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 6, 0x6C6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_307',
    )

    OP_6F(0x0003, 0)

    Jump('loc_30E')

    def _loc_307(): pass

    label('loc_307')

    OP_6F(0x0003, 60)

    def _loc_30E(): pass

    label('loc_30E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 7, 0x6C7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_320',
    )

    OP_6F(0x0005, 0)

    Jump('loc_327')

    def _loc_320(): pass

    label('loc_320')

    OP_6F(0x0005, 60)

    def _loc_327(): pass

    label('loc_327')

    Return()

# id: 0x0002 offset: 0x328
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_33D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_33D(): pass

    label('loc_33D')

    Return()

# id: 0x0003 offset: 0x33E
@scena.Code('func_03_33E')
def func_03_33E():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -238200, 20000, 42800, 0)
    OP_89(0x0001, -239800, 20000, 42800, 0)
    OP_89(0x0002, -239800, 20000, 41200, 0)
    OP_89(0x0003, -238200, 20000, 41200, 0)
    CameraMove(-239000, 0, 42000, 1500)
    Sleep(100)

    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 300)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4306._SN', 134, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x3C9
@scena.Code('func_04_3C9')
def func_04_3C9():
    EventBegin(0x00)
    OP_13(0x00DE)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xDE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0000, 150)
    OP_70(0x0000, 0)
    Yield()
    OP_89(0x0000, -238200, 10000, 42800, 0)
    OP_89(0x0001, -239800, 10000, 42800, 0)
    OP_89(0x0002, -239800, 10000, 41200, 0)
    OP_89(0x0003, -238200, 10000, 41200, 0)
    CameraMove(-239000, 0, 42000, 0)
    OP_73(0x0000)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -238990, 0, 45400, 0)
    OP_89(0x0001, -238990, 0, 45400, 0)
    OP_89(0x0002, -238990, 0, 45400, 0)
    OP_89(0x0003, -238990, 0, 45400, 0)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x48F
@scena.Code('func_05_48F')
def func_05_48F():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -375200, 20000, 55800, 0)
    OP_89(0x0001, -376800, 20000, 55800, 0)
    OP_89(0x0002, -376800, 20000, 54200, 0)
    OP_89(0x0003, -375200, 20000, 54200, 0)
    CameraMove(-376000, 0, 55000, 1500)
    Sleep(100)

    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 300)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4306._SN', 134, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x51A
@scena.Code('func_06_51A')
def func_06_51A():
    EventBegin(0x00)
    OP_13(0x00DE)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xDE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0001, 150)
    OP_70(0x0001, 0)
    Yield()
    OP_89(0x0000, -375200, 10000, 55800, 0)
    OP_89(0x0001, -376800, 10000, 55800, 0)
    OP_89(0x0002, -376800, 10000, 54200, 0)
    OP_89(0x0003, -375200, 10000, 54200, 0)
    CameraMove(-376000, 0, 55000, 0)
    OP_73(0x0001)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -372640, 0, 55030, 90)
    OP_89(0x0001, -372640, 0, 55030, 90)
    OP_89(0x0002, -372640, 0, 55030, 90)
    OP_89(0x0003, -372640, 0, 55030, 90)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x5E0
@scena.Code('func_07_5E0')
def func_07_5E0():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D7, 7, 0x6BF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_782',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 0, 0x6C0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C0',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    SetChrPos(0x0009, -192000, 1500, -77080, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_062F')
    def lambda_062F():
        ChrMoveTo(0x00FE, -192000, 1000, -77080, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_062F)

    @scena.Lambda('lambda_064A')
    def lambda_064A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_064A)

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
    Battle(0x0000030F, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_69B'),
        (0x00000002, 'loc_6AD'),
        (0x00000001, 'loc_6BD'),
        (-1, 'loc_6C0'),
    )

    def _loc_69B(): pass

    label('loc_69B')

    SetScenaFlags(ScenaFlag(0x00D8, 0, 0x6C0))
    OP_6F(0x0004, 60)
    Sleep(500)

    Jump('loc_6C0')

    def _loc_6AD(): pass

    label('loc_6AD')

    OP_6F(0x0004, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_6BD(): pass

    label('loc_6BD')

    OP_B4(0x00)

    Return()

    def _loc_6C0(): pass

    label('loc_6C0')

    If(
        (
            (Expr.Eval, "AddItem(0x0041, 1)"),
            Expr.Return,
        ),
        'loc_712',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '九尾',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D7, 7, 0x6BF))

    Jump('loc_77F')

    def _loc_712(): pass

    label('loc_712')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '九尾',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '九尾',
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

    def _loc_77F(): pass

    label('loc_77F')

    Jump('loc_7B8')

    def _loc_782(): pass

    label('loc_782')

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
    WaitEffect(0x0F, 0x53)
    def _loc_7B8(): pass

    label('loc_7B8')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x7C6
@scena.Code('func_08_7C6')
def func_08_7C6():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 1, 0x6C1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_980',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 2, 0x6C2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8A6',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, -91050, 1500, 43060, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0815')
    def lambda_0815():
        ChrMoveTo(0x00FE, -91050, 1000, 43060, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0815)

    @scena.Lambda('lambda_0830')
    def lambda_0830():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0830)

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
    Battle(0x00000311, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_881'),
        (0x00000002, 'loc_893'),
        (0x00000001, 'loc_8A3'),
        (-1, 'loc_8A6'),
    )

    def _loc_881(): pass

    label('loc_881')

    SetScenaFlags(ScenaFlag(0x00D8, 2, 0x6C2))
    OP_6F(0x0006, 60)
    Sleep(500)

    Jump('loc_8A6')

    def _loc_893(): pass

    label('loc_893')

    OP_6F(0x0006, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_8A3(): pass

    label('loc_8A3')

    OP_B4(0x00)

    Return()

    def _loc_8A6(): pass

    label('loc_8A6')

    If(
        (
            (Expr.Eval, "AddItem(0x00FD, 1)"),
            Expr.Return,
        ),
        'loc_900',
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
    SetScenaFlags(ScenaFlag(0x00D8, 1, 0x6C1))

    Jump('loc_97D')

    def _loc_900(): pass

    label('loc_900')

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
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_97D(): pass

    label('loc_97D')

    Jump('loc_9B6')

    def _loc_980(): pass

    label('loc_980')

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
    WaitEffect(0x0F, 0x54)
    def _loc_9B6(): pass

    label('loc_9B6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x9C4
@scena.Code('func_09_9C4')
def func_09_9C4():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 3, 0x6C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B78',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 4, 0x6C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA4',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    SetChrPos(0x0009, -305690, 1500, 54020, 320)
    ChrTurnDirection(0x0009, 0x0000, 0)

    @scena.Lambda('lambda_0A13')
    def lambda_0A13():
        ChrMoveTo(0x00FE, -305690, 1000, 54020, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A13)

    @scena.Lambda('lambda_0A2E')
    def lambda_0A2E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A2E)

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
    Battle(0x0000030F, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_A7F'),
        (0x00000002, 'loc_A91'),
        (0x00000001, 'loc_AA1'),
        (-1, 'loc_AA4'),
    )

    def _loc_A7F(): pass

    label('loc_A7F')

    SetScenaFlags(ScenaFlag(0x00D8, 4, 0x6C4))
    OP_6F(0x0007, 60)
    Sleep(500)

    Jump('loc_AA4')

    def _loc_A91(): pass

    label('loc_A91')

    OP_6F(0x0007, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_AA1(): pass

    label('loc_AA1')

    OP_B4(0x00)

    Return()

    def _loc_AA4(): pass

    label('loc_AA4')

    If(
        (
            (Expr.Eval, "AddItem(0x009D, 1)"),
            Expr.Return,
        ),
        'loc_AFC',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '狂战士巨刃',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D8, 3, 0x6C3))

    Jump('loc_B75')

    def _loc_AFC(): pass

    label('loc_AFC')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '狂战士巨刃',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '狂战士巨刃',
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

    def _loc_B75(): pass

    label('loc_B75')

    Jump('loc_BAE')

    def _loc_B78(): pass

    label('loc_B78')

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
    WaitEffect(0x0F, 0x55)
    def _loc_BAE(): pass

    label('loc_BAE')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xBBC
@scena.Code('func_0A_BBC')
def func_0A_BBC():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 5, 0x6C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CAC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_C32',
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
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D8, 5, 0x6C5))

    Jump('loc_CA9')

    def _loc_C32(): pass

    label('loc_C32')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
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

    def _loc_CA9(): pass

    label('loc_CA9')

    Jump('loc_CE2')

    def _loc_CAC(): pass

    label('loc_CAC')

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
    WaitEffect(0x0F, 0x56)
    def _loc_CE2(): pass

    label('loc_CE2')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0xCF0
@scena.Code('func_0B_CF0')
def func_0B_CF0():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 6, 0x6C6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FF, 1)"),
            Expr.Return,
        ),
        'loc_D6C',
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
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D8, 6, 0x6C6))

    Jump('loc_DEF')

    def _loc_D6C(): pass

    label('loc_D6C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            'ＥＰ改良填充剂',
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

    def _loc_DEF(): pass

    label('loc_DEF')

    Jump('loc_E28')

    def _loc_DF2(): pass

    label('loc_DF2')

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
    WaitEffect(0x0F, 0x57)
    def _loc_E28(): pass

    label('loc_E28')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000C offset: 0xE36
@scena.Code('func_0C_E36')
def func_0C_E36():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D8, 7, 0x6C7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F26',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F7, 1)"),
            Expr.Return,
        ),
        'loc_EAC',
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
    SetScenaFlags(ScenaFlag(0x00D8, 7, 0x6C7))

    Jump('loc_F23')

    def _loc_EAC(): pass

    label('loc_EAC')

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
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_F23(): pass

    label('loc_F23')

    Jump('loc_F5C')

    def _loc_F26(): pass

    label('loc_F26')

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
    WaitEffect(0x0F, 0x58)
    def _loc_F5C(): pass

    label('loc_F5C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
