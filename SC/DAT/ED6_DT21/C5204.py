import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5204_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5204   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5204.x'
    header.mapIndex       = 1
    header.bgm            = 63
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
        ('ED6_DT29/CH12950._CH', 'ED6_DT29/CH12950P._CP'),
        ('ED6_DT29/CH12951._CH', 'ED6_DT29/CH12951P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT29/CH12960._CH', 'ED6_DT29/CH12960P._CP'),
        ('ED6_DT29/CH12961._CH', 'ED6_DT29/CH12961P._CP'),
        ('ED6_DT29/CH13010._CH', 'ED6_DT29/CH13010P._CP'),
        ('ED6_DT29/CH13011._CH', 'ED6_DT29/CH13011P._CP'),
        ('ED6_DT29/CH12200._CH', 'ED6_DT29/CH12200P._CP'),
        ('ED6_DT29/CH12201._CH', 'ED6_DT29/CH12201P._CP'),
        ('ED6_DT29/CH13020._CH', 'ED6_DT29/CH13020P._CP'),
        ('ED6_DT29/CH13021._CH', 'ED6_DT29/CH13021P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = -150030,
            z                   = 2000,
            y                   = 875370,
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
    )

# id: 0x10002 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 2390,
            z           = 0,
            y           = 76600,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0449,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 100,
            z           = -4000,
            y           = 193690,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0520,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 2770,
            z           = 0,
            y           = 326530,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x044A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -75530,
            z           = 0,
            y           = 464940,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x044B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -147410,
            z           = 0,
            y           = 551800,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x051E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -131350,
            z           = 0,
            y           = 659450,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x051F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -145610,
            z           = 0,
            y           = 674090,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0449,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -245920,
            z           = 0,
            y           = 774830,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x044A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -399040,
            z           = 0,
            y           = 877240,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0520,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x226
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x226
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -72380,
            triggerZ            = 0,
            triggerY            = 194000,
            triggerRange        = 1000,
            actorX              = -73040,
            actorZ              = 0,
            actorY              = 194050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72440,
            triggerZ            = 0,
            triggerY            = 194090,
            triggerRange        = 1000,
            actorX              = 73080,
            actorZ              = 0,
            actorY              = 194160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -150060,
            triggerZ            = 0,
            triggerY            = 874750,
            triggerRange        = 1000,
            actorX              = -150030,
            actorZ              = 0,
            actorY              = 875370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -154610,
            triggerZ            = 0,
            triggerY            = 872080,
            triggerRange        = 1000,
            actorX              = -155230,
            actorZ              = 0,
            actorY              = 872050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -145310,
            triggerZ            = 0,
            triggerY            = 872020,
            triggerRange        = 1000,
            actorX              = -144650,
            actorZ              = 0,
            actorY              = 872050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -253060,
            triggerZ            = 0,
            triggerY            = 874800,
            triggerRange        = 1000,
            actorX              = -253030,
            actorZ              = 0,
            actorY              = 875370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -249970,
            triggerZ            = 0,
            triggerY            = 874740,
            triggerRange        = 1000,
            actorX              = -250040,
            actorZ              = 0,
            actorY              = 875370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -247030,
            triggerZ            = 0,
            triggerY            = 874750,
            triggerRange        = 1000,
            actorX              = -246990,
            actorZ              = 0,
            actorY              = 875370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -107900,
            triggerZ            = 0,
            triggerY            = 465080,
            triggerRange        = 1000,
            actorX              = -108520,
            actorZ              = 0,
            actorY              = 465050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x36A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x36B
@scena.Code('func_01_36B')
def func_01_36B():
    ExecExpressionWithValue(
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 0, 0x2340)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_393',
    )

    OP_6F(0x000E, 0)

    Jump('loc_39A')

    def _loc_393(): pass

    label('loc_393')

    OP_6F(0x000E, 60)

    def _loc_39A(): pass

    label('loc_39A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 1, 0x2341)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AC',
    )

    OP_6F(0x000F, 0)

    Jump('loc_3B3')

    def _loc_3AC(): pass

    label('loc_3AC')

    OP_6F(0x000F, 60)

    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 2, 0x2342)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C5',
    )

    OP_6F(0x0010, 0)

    Jump('loc_3CC')

    def _loc_3C5(): pass

    label('loc_3C5')

    OP_6F(0x0010, 60)

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 4, 0x2344)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DE',
    )

    OP_6F(0x0011, 0)

    Jump('loc_3E5')

    def _loc_3DE(): pass

    label('loc_3DE')

    OP_6F(0x0011, 60)

    def _loc_3E5(): pass

    label('loc_3E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 5, 0x2345)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F7',
    )

    OP_6F(0x0012, 0)

    Jump('loc_3FE')

    def _loc_3F7(): pass

    label('loc_3F7')

    OP_6F(0x0012, 60)

    def _loc_3FE(): pass

    label('loc_3FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 6, 0x2346)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_410',
    )

    OP_6F(0x0013, 0)

    Jump('loc_417')

    def _loc_410(): pass

    label('loc_410')

    OP_6F(0x0013, 60)

    def _loc_417(): pass

    label('loc_417')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 7, 0x2347)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_429',
    )

    OP_6F(0x0014, 0)

    Jump('loc_430')

    def _loc_429(): pass

    label('loc_429')

    OP_6F(0x0014, 60)

    def _loc_430(): pass

    label('loc_430')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 0, 0x2348)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_442',
    )

    OP_6F(0x0015, 0)

    Jump('loc_449')

    def _loc_442(): pass

    label('loc_442')

    OP_6F(0x0015, 60)

    def _loc_449(): pass

    label('loc_449')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 1, 0x2349)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45B',
    )

    OP_6F(0x0016, 0)

    Jump('loc_462')

    def _loc_45B(): pass

    label('loc_45B')

    OP_6F(0x0016, 60)

    def _loc_462(): pass

    label('loc_462')

    Return()

# id: 0x0002 offset: 0x463
@scena.Code('func_02_463')
def func_02_463():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_478',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_463')

    def _loc_478(): pass

    label('loc_478')

    Return()

# id: 0x0003 offset: 0x479
@scena.Code('func_03_479')
def func_03_479():
    UnlockAchievement(0x02, 0x011A, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 0, 0x2340)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000E, 30)
    OP_73(0x000E)
    OP_6F(0x000E, 30)
    AddSepith(0x00, 100)
    AddSepith(0x01, 100)
    AddSepith(0x02, 100)
    AddSepith(0x03, 100)
    AddSepith(0x04, 100)
    AddSepith(0x05, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0468, 0, 0x2340))

    Jump('loc_5BF')

    def _loc_5A5(): pass

    label('loc_5A5')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5BF(): pass

    label('loc_5BF')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5D1
@scena.Code('func_04_5D1')
def func_04_5D1():
    UnlockAchievement(0x02, 0x011B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 1, 0x2341)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6AE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000F, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_645',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0468, 1, 0x2341))

    Jump('loc_6AB')

    def _loc_645(): pass

    label('loc_645')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0)

    def _loc_6AB(): pass

    label('loc_6AB')

    Jump('loc_6DF')

    def _loc_6AE(): pass

    label('loc_6AE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_6DF(): pass

    label('loc_6DF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6ED
@scena.Code('func_05_6ED')
def func_05_6ED():
    UnlockAchievement(0x02, 0x011C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 2, 0x2342)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_885',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0010, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 3, 0x2343)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D1',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0744')
    def lambda_0744():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0744)

    @scena.Lambda('lambda_075F')
    def lambda_075F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_075F)

    ChrClearFlags(0x0008, 0x0080)

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
    Battle(0x00000522, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_7AC'),
        (0x00000002, 'loc_7BE'),
        (0x00000001, 'loc_7CE'),
        (-1, 'loc_7D1'),
    )

    def _loc_7AC(): pass

    label('loc_7AC')

    SetScenaFlags(ScenaFlag(0x0468, 3, 0x2343))
    OP_6F(0x0010, 60)
    Sleep(500)

    Jump('loc_7D1')

    def _loc_7BE(): pass

    label('loc_7BE')

    OP_6F(0x0010, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_7CE(): pass

    label('loc_7CE')

    OP_B4(0x00)

    Return()

    def _loc_7D1(): pass

    label('loc_7D1')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['镜铁靴'], 1)"),
            Expr.Return,
        ),
        'loc_820',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['镜铁靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0468, 2, 0x2342))

    Jump('loc_882')

    def _loc_820(): pass

    label('loc_820')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['镜铁靴']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['镜铁靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0010, 60)
    OP_70(0x0010, 0)

    def _loc_882(): pass

    label('loc_882')

    Jump('loc_8B4')

    def _loc_885(): pass

    label('loc_885')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_8B4(): pass

    label('loc_8B4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8C2
@scena.Code('func_06_8C2')
def func_06_8C2():
    UnlockAchievement(0x02, 0x011D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 4, 0x2344)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_99F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0011, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_936',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0468, 4, 0x2344))

    Jump('loc_99C')

    def _loc_936(): pass

    label('loc_936')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0011, 60)
    OP_70(0x0011, 0)

    def _loc_99C(): pass

    label('loc_99C')

    Jump('loc_9D0')

    def _loc_99F(): pass

    label('loc_99F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_9D0(): pass

    label('loc_9D0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x9DE
@scena.Code('func_07_9DE')
def func_07_9DE():
    UnlockAchievement(0x02, 0x011E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 5, 0x2345)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ABB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0012, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_A52',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0468, 5, 0x2345))

    Jump('loc_AB8')

    def _loc_A52(): pass

    label('loc_A52')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0012, 60)
    OP_70(0x0012, 0)

    def _loc_AB8(): pass

    label('loc_AB8')

    Jump('loc_AEC')

    def _loc_ABB(): pass

    label('loc_ABB')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_AEC(): pass

    label('loc_AEC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xAFA
@scena.Code('func_08_AFA')
def func_08_AFA():
    UnlockAchievement(0x02, 0x011F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 6, 0x2346)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BD7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0013, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_B6E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0468, 6, 0x2346))

    Jump('loc_BD4')

    def _loc_B6E(): pass

    label('loc_B6E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0013, 60)
    OP_70(0x0013, 0)

    def _loc_BD4(): pass

    label('loc_BD4')

    Jump('loc_C08')

    def _loc_BD7(): pass

    label('loc_BD7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_C08(): pass

    label('loc_C08')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xC16
@scena.Code('func_09_C16')
def func_09_C16():
    UnlockAchievement(0x02, 0x0120, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0468, 7, 0x2347)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CF3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0014, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['木耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_C8A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['木耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0468, 7, 0x2347))

    Jump('loc_CF0')

    def _loc_C8A(): pass

    label('loc_C8A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['木耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['木耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0014, 60)
    OP_70(0x0014, 0)

    def _loc_CF0(): pass

    label('loc_CF0')

    Jump('loc_D24')

    def _loc_CF3(): pass

    label('loc_CF3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_D24(): pass

    label('loc_D24')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xD32
@scena.Code('func_0A_D32')
def func_0A_D32():
    UnlockAchievement(0x02, 0x0121, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 0, 0x2348)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E5E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0015, 30)
    OP_73(0x0015)
    OP_6F(0x0015, 30)
    AddSepith(0x00, 100)
    AddSepith(0x01, 100)
    AddSepith(0x02, 100)
    AddSepith(0x03, 100)
    AddSepith(0x04, 100)
    AddSepith(0x05, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0469, 0, 0x2348))

    Jump('loc_E78')

    def _loc_E5E(): pass

    label('loc_E5E')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_E78(): pass

    label('loc_E78')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0xE8A
@scena.Code('func_0B_E8A')
def func_0B_E8A():
    UnlockAchievement(0x02, 0x0122, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0469, 1, 0x2349)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F67',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0016, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_EFE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0469, 1, 0x2349))

    Jump('loc_F64')

    def _loc_EFE(): pass

    label('loc_EFE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0016, 60)
    OP_70(0x0016, 0)

    def _loc_F64(): pass

    label('loc_F64')

    Jump('loc_F98')

    def _loc_F67(): pass

    label('loc_F67')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_F98(): pass

    label('loc_F98')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
