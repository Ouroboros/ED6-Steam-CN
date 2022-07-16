import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4308_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4308   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4308.x'
    header.mapIndex       = 1
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xB21
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
        ('ED6_DT09/CH10950._CH', 'ED6_DT09/CH10950P._CP'),
        ('ED6_DT09/CH10951._CH', 'ED6_DT09/CH10951P._CP'),
        ('ED6_DT09/CH10920._CH', 'ED6_DT09/CH10920P._CP'),
        ('ED6_DT09/CH10921._CH', 'ED6_DT09/CH10921P._CP'),
        ('ED6_DT09/CH10940._CH', 'ED6_DT09/CH10940P._CP'),
        ('ED6_DT09/CH10941._CH', 'ED6_DT09/CH10941P._CP'),
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -83130,
            z           = 0,
            y           = 68890,
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
            x           = -189080,
            z           = 0,
            y           = -151150,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x028F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3000,
            y           = -1000,
            z           = 156000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -170000,
            y           = -1000,
            z           = 72000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -201000,
            y           = -1000,
            z           = -86000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x1B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -265110,
            triggerZ            = 0,
            triggerY            = -137400,
            triggerRange        = 1000,
            actorX              = -265080,
            actorZ              = 0,
            actorY              = -136680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -187270,
            triggerZ            = 0,
            triggerY            = -290980,
            triggerRange        = 1000,
            actorX              = -188020,
            actorZ              = 0,
            actorY              = -291100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -129000,
            triggerZ            = 0,
            triggerY            = -229340,
            triggerRange        = 1000,
            actorX              = -129000,
            actorZ              = 0,
            actorY              = -228660,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x21E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_22C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0004)

    def _loc_22C(): pass

    label('loc_22C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_23A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0006)

    def _loc_23A(): pass

    label('loc_23A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_248',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0008)

    def _loc_248(): pass

    label('loc_248')

    Return()

# id: 0x0001 offset: 0x249
@scena.Code('Init')
def Init():
    OP_10(0x14, 0x00)
    OP_10(0x13, 0x00)
    OP_10(0x12, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 5, 0x6AD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_264',
    )

    OP_6F(0x0005, 0)

    Jump('loc_26B')

    def _loc_264(): pass

    label('loc_264')

    OP_6F(0x0005, 60)

    def _loc_26B(): pass

    label('loc_26B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 7, 0x6AF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27D',
    )

    OP_6F(0x0003, 0)

    Jump('loc_284')

    def _loc_27D(): pass

    label('loc_27D')

    OP_6F(0x0003, 60)

    def _loc_284(): pass

    label('loc_284')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 0, 0x6B0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_296',
    )

    OP_6F(0x0004, 0)

    Jump('loc_29D')

    def _loc_296(): pass

    label('loc_296')

    OP_6F(0x0004, 60)

    def _loc_29D(): pass

    label('loc_29D')

    Return()

# id: 0x0002 offset: 0x29E
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2B3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2B3(): pass

    label('loc_2B3')

    Return()

# id: 0x0003 offset: 0x2B4
@scena.Code('func_03_2B4')
def func_03_2B4():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -2200, 20000, 156800, 0)
    OP_89(0x0001, -3800, 20000, 156800, 0)
    OP_89(0x0002, -3800, 20000, 155200, 0)
    OP_89(0x0003, -2200, 20000, 155200, 0)
    CameraMove(-3000, 0, 156000, 1500)
    Sleep(100)

    OP_B0(0x0000, 0x5A)
    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 1600)
    OP_70(0x0000, 1000)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4307._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x343
@scena.Code('func_04_343')
def func_04_343():
    EventBegin(0x00)
    OP_13(0x00E0)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xE0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0000, 1300)
    OP_70(0x0000, 1600)
    Yield()
    OP_89(0x0000, -2200, 20000, 156800, 0)
    OP_89(0x0001, -3800, 20000, 156800, 0)
    OP_89(0x0002, -3800, 20000, 155200, 0)
    OP_89(0x0003, -2200, 20000, 155200, 0)
    CameraMove(-3000, 0, 156000, 0)
    OP_73(0x0000)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -3030, 0, 152600, 180)
    OP_89(0x0001, -3030, 0, 152600, 180)
    OP_89(0x0002, -3030, 0, 152600, 180)
    OP_89(0x0003, -3030, 0, 152600, 180)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x409
@scena.Code('func_05_409')
def func_05_409():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -169200, 20000, 72800, 0)
    OP_89(0x0001, -170800, 20000, 72800, 0)
    OP_89(0x0002, -170800, 20000, 71200, 0)
    OP_89(0x0003, -169200, 20000, 71200, 0)
    CameraMove(-170000, 0, 72000, 1500)
    Sleep(100)

    OP_B0(0x0001, 0x5A)
    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0001, 1600)
    OP_70(0x0001, 1000)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/C4306._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x498
@scena.Code('func_06_498')
def func_06_498():
    EventBegin(0x00)
    OP_13(0x00E0)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xE0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0001, 1300)
    OP_70(0x0001, 1600)
    Yield()
    OP_89(0x0000, -169200, 20000, 72800, 0)
    OP_89(0x0001, -170800, 20000, 72800, 0)
    OP_89(0x0002, -170800, 20000, 71200, 0)
    OP_89(0x0003, -169200, 20000, 71200, 0)
    CameraMove(-170000, 0, 72000, 0)
    OP_73(0x0001)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -166430, 0, 72020, 90)
    OP_89(0x0001, -166430, 0, 72020, 90)
    OP_89(0x0002, -166430, 0, 72020, 90)
    OP_89(0x0003, -166430, 0, 72020, 90)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x55E
@scena.Code('func_07_55E')
def func_07_55E():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -200200, 20000, -86800, 0)
    OP_89(0x0001, -201800, 20000, -86800, 0)
    OP_89(0x0002, -201800, 20000, -85200, 0)
    OP_89(0x0003, -200200, 20000, -85200, 0)
    CameraMove(-201000, 0, -86000, 1500)
    Sleep(100)

    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 300)
    Sleep(4000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x5E9
@scena.Code('func_08_5E9')
def func_08_5E9():
    EventBegin(0x00)
    OP_13(0x00E0)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xE0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0002, 150)
    OP_70(0x0002, 0)
    Yield()
    OP_89(0x0000, -200200, 20000, -86800, 0)
    OP_89(0x0001, -201800, 20000, -86800, 0)
    OP_89(0x0002, -201800, 20000, -85200, 0)
    OP_89(0x0003, -200200, 20000, -85200, 0)
    CameraMove(-201000, 0, -86000, 0)
    OP_73(0x0002)
    Sleep(100)

    Fade(1000)
    OP_89(0x0000, -200910, 0, -89200, 180)
    OP_89(0x0001, -200910, 0, -89200, 180)
    OP_89(0x0002, -200910, 0, -89200, 180)
    OP_89(0x0003, -200910, 0, -89200, 180)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x6AF
@scena.Code('func_09_6AF')
def func_09_6AF():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 5, 0x6AD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_85D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 6, 0x6AE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_78F',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    SetChrPos(0x0008, -265080, 1500, -136680, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_06FE')
    def lambda_06FE():
        ChrMoveTo(0x00FE, -265080, 1000, -136680, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_06FE)

    @scena.Lambda('lambda_0719')
    def lambda_0719():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0719)

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
    Battle(0x00000313, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_76A'),
        (0x00000002, 'loc_77C'),
        (0x00000001, 'loc_78C'),
        (-1, 'loc_78F'),
    )

    def _loc_76A(): pass

    label('loc_76A')

    SetScenaFlags(ScenaFlag(0x00D5, 6, 0x6AE))
    OP_6F(0x0005, 60)
    Sleep(500)

    Jump('loc_78F')

    def _loc_77C(): pass

    label('loc_77C')

    OP_6F(0x0005, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_78C(): pass

    label('loc_78C')

    OP_B4(0x00)

    Return()

    def _loc_78F(): pass

    label('loc_78F')

    If(
        (
            (Expr.Eval, "AddItem(0x0119, 1)"),
            Expr.Return,
        ),
        'loc_7E5',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '天神之靴',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00D5, 5, 0x6AD))

    Jump('loc_85A')

    def _loc_7E5(): pass

    label('loc_7E5')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '天神之靴',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '天神之靴',
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

    def _loc_85A(): pass

    label('loc_85A')

    Jump('loc_893')

    def _loc_85D(): pass

    label('loc_85D')

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
    WaitEffect(0x0F, 0x62)
    def _loc_893(): pass

    label('loc_893')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x8A1
@scena.Code('func_0A_8A1')
def func_0A_8A1():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D5, 7, 0x6AF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_991',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_917',
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
    SetScenaFlags(ScenaFlag(0x00D5, 7, 0x6AF))

    Jump('loc_98E')

    def _loc_917(): pass

    label('loc_917')

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
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_98E(): pass

    label('loc_98E')

    Jump('loc_9C7')

    def _loc_991(): pass

    label('loc_991')

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
    WaitEffect(0x0F, 0x63)
    def _loc_9C7(): pass

    label('loc_9C7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x9D5
@scena.Code('func_0B_9D5')
def func_0B_9D5():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D6, 0, 0x6B0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_A4B',
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
    SetScenaFlags(ScenaFlag(0x00D6, 0, 0x6B0))

    Jump('loc_AC2')

    def _loc_A4B(): pass

    label('loc_A4B')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_AC2(): pass

    label('loc_AC2')

    Jump('loc_AFB')

    def _loc_AC5(): pass

    label('loc_AC5')

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
    WaitEffect(0x0F, 0x64)
    def _loc_AFB(): pass

    label('loc_AFB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
