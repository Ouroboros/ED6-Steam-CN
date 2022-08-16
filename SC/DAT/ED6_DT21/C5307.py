import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5307_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5307   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5307.x'
    header.mapIndex       = 1
    header.bgm            = 64
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
        ('ED6_DT29/CH12420._CH', 'ED6_DT29/CH12420P._CP'),
        ('ED6_DT29/CH12421._CH', 'ED6_DT29/CH12421P._CP'),
        ('ED6_DT29/CH12280._CH', 'ED6_DT29/CH12280P._CP'),
        ('ED6_DT29/CH12281._CH', 'ED6_DT29/CH12281P._CP'),
        ('ED6_DT29/CH12300._CH', 'ED6_DT29/CH12300P._CP'),
        ('ED6_DT29/CH12301._CH', 'ED6_DT29/CH12301P._CP'),
        ('ED6_DT29/CH12290._CH', 'ED6_DT29/CH12290P._CP'),
        ('ED6_DT29/CH12291._CH', 'ED6_DT29/CH12291P._CP'),
        ('ED6_DT29/CH12340._CH', 'ED6_DT29/CH12340P._CP'),
        ('ED6_DT29/CH12341._CH', 'ED6_DT29/CH12341P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '升降梯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
            name                = '',
            x                   = -107060,
            z                   = 1500,
            y                   = 9030,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -91860,
            z           = 2170,
            y           = 97190,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -99300,
            z           = 50,
            y           = 8630,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0530,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -78310,
            z           = 2690,
            y           = -74320,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 84130,
            z           = 2220,
            y           = -84980,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x052E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 5170,
            y           = -2000,
            z           = 110010,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = 100000,
            y           = -2000,
            z           = 9010,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000A,
        ),
    )

# id: 0x10004 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -105100,
            triggerZ            = 0,
            triggerY            = 3560,
            triggerRange        = 1000,
            actorX              = -105130,
            actorZ              = 0,
            actorY              = 2950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -106430,
            triggerZ            = 0,
            triggerY            = 9060,
            triggerRange        = 1000,
            actorX              = -107060,
            actorZ              = 0,
            actorY              = 9030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -105100,
            triggerZ            = 0,
            triggerY            = 14350,
            triggerRange        = 1000,
            actorX              = -105070,
            actorZ              = 0,
            actorY              = 15000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -92920,
            triggerZ            = 0,
            triggerY            = 14350,
            triggerRange        = 1000,
            actorX              = -92880,
            actorZ              = 0,
            actorY              = 15030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -91440,
            triggerZ            = 0,
            triggerY            = 8950,
            triggerRange        = 1000,
            actorX              = -90840,
            actorZ              = 0,
            actorY              = 8980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -93070,
            triggerZ            = 0,
            triggerY            = 3650,
            triggerRange        = 1000,
            actorX              = -92940,
            actorZ              = 0,
            actorY              = 2970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -710,
            triggerZ            = 2000,
            triggerY            = -93980,
            triggerRange        = 1000,
            actorX              = -80,
            actorZ              = 2000,
            actorY              = -93950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 92130,
            triggerZ            = 8000,
            triggerY            = -57040,
            triggerRange        = 1200,
            actorX              = 92130,
            actorZ              = 9200,
            actorY              = -57040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x30A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31A',
    )

    Event(0, func_0C_106A)

    def _loc_31A(): pass

    label('loc_31A')

    Return()

# id: 0x0001 offset: 0x31B
@scena.Code('func_01_31B')
def func_01_31B():
    ExecExpressionWithValue(
        0x000A,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xEF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 0, 0x2390)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_359',
    )

    OP_6F(0x0002, 0)

    Jump('loc_360')

    def _loc_359(): pass

    label('loc_359')

    OP_6F(0x0002, 60)

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 1, 0x2391)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_372',
    )

    OP_6F(0x0003, 0)

    Jump('loc_379')

    def _loc_372(): pass

    label('loc_372')

    OP_6F(0x0003, 60)

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 3, 0x2393)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38B',
    )

    OP_6F(0x0004, 0)

    Jump('loc_392')

    def _loc_38B(): pass

    label('loc_38B')

    OP_6F(0x0004, 60)

    def _loc_392(): pass

    label('loc_392')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 4, 0x2394)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A4',
    )

    OP_6F(0x0005, 0)

    Jump('loc_3AB')

    def _loc_3A4(): pass

    label('loc_3A4')

    OP_6F(0x0005, 60)

    def _loc_3AB(): pass

    label('loc_3AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 5, 0x2395)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BD',
    )

    OP_6F(0x0006, 0)

    Jump('loc_3C4')

    def _loc_3BD(): pass

    label('loc_3BD')

    OP_6F(0x0006, 60)

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 7, 0x2397)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D6',
    )

    OP_6F(0x0007, 0)

    Jump('loc_3DD')

    def _loc_3D6(): pass

    label('loc_3D6')

    OP_6F(0x0007, 60)

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0473, 0, 0x2398)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EF',
    )

    OP_6F(0x0008, 0)

    Jump('loc_3F6')

    def _loc_3EF(): pass

    label('loc_3EF')

    OP_6F(0x0008, 60)

    def _loc_3F6(): pass

    label('loc_3F6')

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x00)
    PlaySE(320, 0x00, 0x64)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_46C',
    )

    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 92130, 9200, -57040, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0009, 0x0020)
    OP_6F(0x0009, 0)
    OP_70(0x0009, 250)

    Jump('loc_478')

    def _loc_46C(): pass

    label('loc_46C')

    OP_72(0x0009, 0x0020)
    OP_6F(0x0009, 250)

    def _loc_478(): pass

    label('loc_478')

    Return()

# id: 0x0002 offset: 0x479
@scena.Code('func_02_479')
def func_02_479():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_48E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_479')

    def _loc_48E(): pass

    label('loc_48E')

    Return()

# id: 0x0003 offset: 0x48F
@scena.Code('func_03_48F')
def func_03_48F():
    UnlockAchievement(0x02, 0x014C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 0, 0x2390)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_503',
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
    SetScenaFlags(ScenaFlag(0x0472, 0, 0x2390))

    Jump('loc_569')

    def _loc_503(): pass

    label('loc_503')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_569(): pass

    label('loc_569')

    Jump('loc_59D')

    def _loc_56C(): pass

    label('loc_56C')

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
    def _loc_59D(): pass

    label('loc_59D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5AB
@scena.Code('func_04_5AB')
def func_04_5AB():
    UnlockAchievement(0x02, 0x014D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 1, 0x2391)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_743',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 2, 0x2392)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68F',
    )

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0009, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0009, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0602')
    def lambda_0602():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0602)

    @scena.Lambda('lambda_061D')
    def lambda_061D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_061D)

    ChrClearFlags(0x0009, 0x0080)

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
    Battle(0x00000532, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0009, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_66A'),
        (0x00000002, 'loc_67C'),
        (0x00000001, 'loc_68C'),
        (-1, 'loc_68F'),
    )

    def _loc_66A(): pass

    label('loc_66A')

    SetScenaFlags(ScenaFlag(0x0472, 2, 0x2392))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_68F')

    def _loc_67C(): pass

    label('loc_67C')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_68C(): pass

    label('loc_68C')

    OP_B4(0x00)

    Return()

    def _loc_68F(): pass

    label('loc_68F')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['光之环'], 1)"),
            Expr.Return,
        ),
        'loc_6DE',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['光之环']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0472, 1, 0x2391))

    Jump('loc_740')

    def _loc_6DE(): pass

    label('loc_6DE')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['光之环']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['光之环']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_740(): pass

    label('loc_740')

    Jump('loc_772')

    def _loc_743(): pass

    label('loc_743')

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
    def _loc_772(): pass

    label('loc_772')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x780
@scena.Code('func_05_780')
def func_05_780():
    UnlockAchievement(0x02, 0x014E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 3, 0x2393)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_85D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_7F4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0472, 3, 0x2393))

    Jump('loc_85A')

    def _loc_7F4(): pass

    label('loc_7F4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_85A(): pass

    label('loc_85A')

    Jump('loc_88E')

    def _loc_85D(): pass

    label('loc_85D')

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
    def _loc_88E(): pass

    label('loc_88E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x89C
@scena.Code('func_06_89C')
def func_06_89C():
    UnlockAchievement(0x02, 0x014F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 4, 0x2394)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_979',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_910',
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
    SetScenaFlags(ScenaFlag(0x0472, 4, 0x2394))

    Jump('loc_976')

    def _loc_910(): pass

    label('loc_910')

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
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_976(): pass

    label('loc_976')

    Jump('loc_9AA')

    def _loc_979(): pass

    label('loc_979')

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
    def _loc_9AA(): pass

    label('loc_9AA')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x9B8
@scena.Code('func_07_9B8')
def func_07_9B8():
    UnlockAchievement(0x02, 0x0150, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 5, 0x2395)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AE4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 30)
    OP_73(0x0006)
    OP_6F(0x0006, 30)
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
    SetScenaFlags(ScenaFlag(0x0472, 5, 0x2395))

    Jump('loc_AFE')

    def _loc_AE4(): pass

    label('loc_AE4')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_AFE(): pass

    label('loc_AFE')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xB10
@scena.Code('func_08_B10')
def func_08_B10():
    UnlockAchievement(0x02, 0x0151, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0472, 7, 0x2397)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BED',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_B84',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0472, 7, 0x2397))

    Jump('loc_BEA')

    def _loc_B84(): pass

    label('loc_B84')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_BEA(): pass

    label('loc_BEA')

    Jump('loc_C1E')

    def _loc_BED(): pass

    label('loc_BED')

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
    def _loc_C1E(): pass

    label('loc_C1E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xC2C
@scena.Code('func_09_C2C')
def func_09_C2C():
    UnlockAchievement(0x02, 0x0152, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0473, 0, 0x2398)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D09',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['女战士机甲'], 1)"),
            Expr.Return,
        ),
        'loc_CA0',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['女战士机甲']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0473, 0, 0x2398))

    Jump('loc_D06')

    def _loc_CA0(): pass

    label('loc_CA0')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['女战士机甲']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['女战士机甲']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_D06(): pass

    label('loc_D06')

    Jump('loc_D3A')

    def _loc_D09(): pass

    label('loc_D09')

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
    def _loc_D3A(): pass

    label('loc_D3A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xD48
@scena.Code('func_0A_D48')
def func_0A_D48():
    EventBegin(0x00)
    FadeIn(0, 0)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, 100000, -1750, 9010, 0)
    Yield()
    Fade(1000)
    CameraMove(100000, 0, 9010, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 100000, 0, 10010, 0)
    OP_89(0x0001, 101000, 0, 9010, 90)
    OP_89(0x0002, 99000, 0, 9010, 270)
    OP_89(0x0003, 100000, 0, 8010, 180)
    OP_0D()
    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0E01')
    def lambda_0E01():
        ChrMoveTo(0x00FE, 100000, 65000, 9010, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E01)

    Sleep(500)

    @scena.Lambda('lambda_0E21')
    def lambda_0E21():
        CameraMove(100000, 35000, 9010, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E21)

    @scena.Lambda('lambda_0E39')
    def lambda_0E39():
        OP_67(0, 14000, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0E39)

    @scena.Lambda('lambda_0E51')
    def lambda_0E51():
        OP_6C(335000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E51)

    Sleep(500)

    @scena.Lambda('lambda_0E66')
    def lambda_0E66():
        ChrMoveTo(0x00FE, 100000, 65000, 9010, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E66)

    Sleep(500)

    @scena.Lambda('lambda_0E86')
    def lambda_0E86():
        ChrMoveTo(0x00FE, 100000, 65000, 9010, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E86)

    Sleep(400)

    @scena.Lambda('lambda_0EA6')
    def lambda_0EA6():
        ChrMoveTo(0x00FE, 100000, 65000, 9010, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0EA6)

    Sleep(200)

    @scena.Lambda('lambda_0EC6')
    def lambda_0EC6():
        ChrMoveTo(0x00FE, 100000, 65000, 9010, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0EC6)

    Sleep(100)

    @scena.Lambda('lambda_0EE6')
    def lambda_0EE6():
        ChrMoveTo(0x00FE, 100000, 65000, 9010, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0EE6)

    Sleep(2000)

    Sleep(2000)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0451, 4, 0x228C))
    ClearScenaFlags(ScenaFlag(0x0451, 5, 0x228D))
    ClearScenaFlags(ScenaFlag(0x0451, 6, 0x228E))
    ClearScenaFlags(ScenaFlag(0x0451, 7, 0x228F))
    ClearScenaFlags(ScenaFlag(0x0452, 0, 0x2290))
    ClearScenaFlags(ScenaFlag(0x0452, 1, 0x2291))
    ClearScenaFlags(ScenaFlag(0x0452, 2, 0x2292))
    ClearScenaFlags(ScenaFlag(0x0452, 3, 0x2293))
    ClearScenaFlags(ScenaFlag(0x0452, 4, 0x2294))
    SetScenaFlags(ScenaFlag(0x0452, 5, 0x2295))
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0xF3D
@scena.Code('func_0B_F3D')
def func_0B_F3D():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0001)
    ChrSetPos(0x0008, 5170, -1750, 110010, 90)
    Yield()
    Fade(1000)
    CameraMove(5170, 0, 110010, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(298000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 0, 111000, 0)
    OP_89(0x0001, 6000, 0, 110000, 90)
    OP_89(0x0002, 4000, 0, 110000, 270)
    OP_89(0x0003, 5000, 0, 109000, 180)
    OP_0D()
    Sleep(300)

    MapSetFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_0FF2')
    def lambda_0FF2():
        OP_67(0, 6500, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FF2)

    @scena.Lambda('lambda_100A')
    def lambda_100A():
        CameraSetDistance(3700, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_100A)

    @scena.Lambda('lambda_101A')
    def lambda_101A():
        ChrMoveToRelativeAsync(0x00FE, 0, -10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_101A)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0451, 4, 0x228C))
    ClearScenaFlags(ScenaFlag(0x0451, 5, 0x228D))
    ClearScenaFlags(ScenaFlag(0x0451, 6, 0x228E))
    ClearScenaFlags(ScenaFlag(0x0451, 7, 0x228F))
    ClearScenaFlags(ScenaFlag(0x0452, 0, 0x2290))
    ClearScenaFlags(ScenaFlag(0x0452, 1, 0x2291))
    ClearScenaFlags(ScenaFlag(0x0452, 2, 0x2292))
    ClearScenaFlags(ScenaFlag(0x0452, 3, 0x2293))
    ClearScenaFlags(ScenaFlag(0x0452, 4, 0x2294))
    SetScenaFlags(ScenaFlag(0x0452, 5, 0x2295))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x106A
@scena.Code('func_0C_106A')
def func_0C_106A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0001)
    ChrSetPos(0x0008, 5170, -11750, 110010, 90)
    Yield()
    CameraMove(5170, 0, 110010, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 5000, 0, 111000, 0)
    OP_89(0x0001, 6000, 0, 110000, 90)
    OP_89(0x0002, 4000, 0, 110000, 270)
    OP_89(0x0003, 5000, 0, 109000, 180)
    PlaySE(235, 0x00, 0x64)

    @scena.Lambda('lambda_1119')
    def lambda_1119():
        CameraSetDistance(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1119)

    FadeIn(1000, 0)
    OP_13(0x0121)

    @scena.Lambda('lambda_1135')
    def lambda_1135():
        ChrMoveToRelativeAsync(0x00FE, 0, 10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1135)

    Sleep(2200)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    Fade(1000)
    ChrSetPos(0x0000, 20, 0, 109960, 270)
    ChrSetPos(0x0001, 20, 0, 109960, 270)
    ChrSetPos(0x0002, 20, 0, 109960, 270)
    ChrSetPos(0x0003, 20, 0, 109960, 270)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x1206
@scena.Code('func_0D_1206')
def func_0D_1206():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1259',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_13FB')

    def _loc_1259(): pass

    label('loc_1259')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13E0',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0009, 0x0020)
    OP_6F(0x0009, 300)
    OP_70(0x0009, 500)
    OP_73(0x0009)
    OP_6F(0x0009, 500)
    OP_70(0x0009, 700)
    OP_71(0x0009, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x00, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 92130, 9200, -57040, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0x00, 0x00FF, 92130, 9200, -57040, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0009, 0)
    OP_70(0x0009, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_13E0(): pass

    label('loc_13E0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13FA',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_13FA(): pass

    label('loc_13FA')

    Return()

    def _loc_13FB(): pass

    label('loc_13FB')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
