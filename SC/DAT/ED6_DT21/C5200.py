import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5200.x'
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
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 95050,
            z                   = 7000,
            y                   = -69760,
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

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -53380,
            z           = -4000,
            y           = 122950,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -28750,
            z           = -4000,
            y           = 122990,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 155140,
            z           = 0,
            y           = 23120,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 47170,
            z           = 0,
            y           = 58660,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 66780,
            z           = -2000,
            y           = -74110,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 88840,
            z           = 0,
            y           = -179320,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -70750,
            z           = 0,
            y           = -129720,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 59740,
            z           = 2000,
            y           = -63590,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 84410,
            z           = 2000,
            y           = -84740,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1E6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1E6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 53090,
            triggerZ            = 0,
            triggerY            = 206880,
            triggerRange        = 800,
            actorX              = 53490,
            actorZ              = 1200,
            actorY              = 206980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 49220,
            triggerZ            = 0,
            triggerY            = 207080,
            triggerRange        = 800,
            actorX              = 49220,
            actorZ              = 1300,
            actorY              = 207080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -119070,
            triggerZ            = 0,
            triggerY            = -112040,
            triggerRange        = 1000,
            actorX              = -119730,
            actorZ              = 0,
            actorY              = -112040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -119160,
            triggerZ            = 0,
            triggerY            = -162000,
            triggerRange        = 1000,
            actorX              = -119780,
            actorZ              = 0,
            actorY              = -162000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 36940,
            triggerZ            = 0,
            triggerY            = -242420,
            triggerRange        = 1000,
            actorX              = 36940,
            actorZ              = 0,
            actorY              = -243040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 88900,
            triggerZ            = 0,
            triggerY            = -240840,
            triggerRange        = 1000,
            actorX              = 88900,
            actorZ              = 0,
            actorY              = -241500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 96460,
            triggerZ            = 0,
            triggerY            = 23070,
            triggerRange        = 1000,
            actorX              = 97120,
            actorZ              = 0,
            actorY              = 23070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 95050,
            triggerZ            = 6000,
            triggerY            = -69050,
            triggerRange        = 1000,
            actorX              = 95050,
            actorZ              = 6000,
            actorY              = -69760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57620,
            triggerZ            = 2000,
            triggerY            = -61400,
            triggerRange        = 1000,
            actorX              = 57160,
            actorZ              = 2000,
            actorY              = -60930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x32B
@scena.Code('func_01_32B')
def func_01_32B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 0, 0x2300)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33D',
    )

    OP_6F(0x0013, 0)

    Jump('loc_344')

    def _loc_33D(): pass

    label('loc_33D')

    OP_6F(0x0013, 60)

    def _loc_344(): pass

    label('loc_344')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 1, 0x2301)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_356',
    )

    OP_6F(0x0014, 0)

    Jump('loc_35D')

    def _loc_356(): pass

    label('loc_356')

    OP_6F(0x0014, 60)

    def _loc_35D(): pass

    label('loc_35D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 2, 0x2302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36F',
    )

    OP_6F(0x0015, 0)

    Jump('loc_376')

    def _loc_36F(): pass

    label('loc_36F')

    OP_6F(0x0015, 60)

    def _loc_376(): pass

    label('loc_376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 3, 0x2303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_388',
    )

    OP_6F(0x0016, 0)

    Jump('loc_38F')

    def _loc_388(): pass

    label('loc_388')

    OP_6F(0x0016, 60)

    def _loc_38F(): pass

    label('loc_38F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 4, 0x2304)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A1',
    )

    OP_6F(0x0017, 0)

    Jump('loc_3A8')

    def _loc_3A1(): pass

    label('loc_3A1')

    OP_6F(0x0017, 60)

    def _loc_3A8(): pass

    label('loc_3A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 5, 0x2305)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BA',
    )

    OP_6F(0x0018, 0)

    Jump('loc_3C1')

    def _loc_3BA(): pass

    label('loc_3BA')

    OP_6F(0x0018, 60)

    def _loc_3C1(): pass

    label('loc_3C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 7, 0x2307)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D3',
    )

    OP_6F(0x0019, 0)

    Jump('loc_3DA')

    def _loc_3D3(): pass

    label('loc_3D3')

    OP_6F(0x0019, 60)

    def _loc_3DA(): pass

    label('loc_3DA')

    Return()

# id: 0x0002 offset: 0x3DB
@scena.Code('func_02_3DB')
def func_02_3DB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3DB')

    def _loc_3F0(): pass

    label('loc_3F0')

    Return()

# id: 0x0003 offset: 0x3F1
@scena.Code('func_03_3F1')
def func_03_3F1():
    UnlockAchievement(0x02, 0x0109, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 0, 0x2300)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0013, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_465',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0460, 0, 0x2300))

    Jump('loc_4CB')

    def _loc_465(): pass

    label('loc_465')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
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

    def _loc_4CB(): pass

    label('loc_4CB')

    Jump('loc_4FF')

    def _loc_4CE(): pass

    label('loc_4CE')

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
    def _loc_4FF(): pass

    label('loc_4FF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x50D
@scena.Code('func_04_50D')
def func_04_50D():
    UnlockAchievement(0x02, 0x010A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 1, 0x2301)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5EA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0014, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_581',
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
    SetScenaFlags(ScenaFlag(0x0460, 1, 0x2301))

    Jump('loc_5E7')

    def _loc_581(): pass

    label('loc_581')

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
    OP_6F(0x0014, 60)
    OP_70(0x0014, 0)

    def _loc_5E7(): pass

    label('loc_5E7')

    Jump('loc_61B')

    def _loc_5EA(): pass

    label('loc_5EA')

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
    def _loc_61B(): pass

    label('loc_61B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x629
@scena.Code('func_05_629')
def func_05_629():
    UnlockAchievement(0x02, 0x010B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 2, 0x2302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_706',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0015, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_69D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0460, 2, 0x2302))

    Jump('loc_703')

    def _loc_69D(): pass

    label('loc_69D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0015, 60)
    OP_70(0x0015, 0)

    def _loc_703(): pass

    label('loc_703')

    Jump('loc_737')

    def _loc_706(): pass

    label('loc_706')

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
    def _loc_737(): pass

    label('loc_737')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x745
@scena.Code('func_06_745')
def func_06_745():
    UnlockAchievement(0x02, 0x010C, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 3, 0x2303)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_871',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0016, 30)
    OP_73(0x0016)
    OP_6F(0x0016, 30)
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
    SetScenaFlags(ScenaFlag(0x0460, 3, 0x2303))

    Jump('loc_88B')

    def _loc_871(): pass

    label('loc_871')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_88B(): pass

    label('loc_88B')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x89D
@scena.Code('func_07_89D')
def func_07_89D():
    UnlockAchievement(0x02, 0x010D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 4, 0x2304)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_97A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0017, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['银耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_911',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['银耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0460, 4, 0x2304))

    Jump('loc_977')

    def _loc_911(): pass

    label('loc_911')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['银耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['银耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0017, 60)
    OP_70(0x0017, 0)

    def _loc_977(): pass

    label('loc_977')

    Jump('loc_9AB')

    def _loc_97A(): pass

    label('loc_97A')

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
    def _loc_9AB(): pass

    label('loc_9AB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x9B9
@scena.Code('func_08_9B9')
def func_08_9B9():
    UnlockAchievement(0x02, 0x010E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 5, 0x2305)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B51',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0018, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 6, 0x2306)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A9D',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0A10')
    def lambda_0A10():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A10)

    @scena.Lambda('lambda_0A2B')
    def lambda_0A2B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0A2B)

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
    Battle(0x0000043D, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_A78'),
        (0x00000002, 'loc_A8A'),
        (0x00000001, 'loc_A9A'),
        (-1, 'loc_A9D'),
    )

    def _loc_A78(): pass

    label('loc_A78')

    SetScenaFlags(ScenaFlag(0x0460, 6, 0x2306))
    OP_6F(0x0018, 60)
    Sleep(500)

    Jump('loc_A9D')

    def _loc_A8A(): pass

    label('loc_A8A')

    OP_6F(0x0018, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_A9A(): pass

    label('loc_A9A')

    OP_B4(0x00)

    Return()

    def _loc_A9D(): pass

    label('loc_A9D')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['七耀神权'], 1)"),
            Expr.Return,
        ),
        'loc_AEC',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['七耀神权']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0460, 5, 0x2305))

    Jump('loc_B4E')

    def _loc_AEC(): pass

    label('loc_AEC')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['七耀神权']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['七耀神权']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0018, 60)
    OP_70(0x0018, 0)

    def _loc_B4E(): pass

    label('loc_B4E')

    Jump('loc_B80')

    def _loc_B51(): pass

    label('loc_B51')

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
    def _loc_B80(): pass

    label('loc_B80')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xB8E
@scena.Code('func_09_B8E')
def func_09_B8E():
    UnlockAchievement(0x02, 0x010F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0460, 7, 0x2307)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C6B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0019, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['黑耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_C02',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['黑耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0460, 7, 0x2307))

    Jump('loc_C68')

    def _loc_C02(): pass

    label('loc_C02')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['黑耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['黑耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0019, 60)
    OP_70(0x0019, 0)

    def _loc_C68(): pass

    label('loc_C68')

    Jump('loc_C9C')

    def _loc_C6B(): pass

    label('loc_C6B')

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
    def _loc_C9C(): pass

    label('loc_C9C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xCAA
@scena.Code('func_0A_CAA')
def func_0A_CAA():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门坚固地锁着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0xCE0
@scena.Code('func_0B_CE0')
def func_0B_CE0():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【紧急避难通道】\n',
            '卡尔玛丽≌ 中枢塔',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '只有在来自『中枢塔』的\n',
            '导力供给产生异常的情况下\n',
            '才会自动解除锁定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '此外，门附近\n',
            '禁止放置会对避难\n',
            '造成障碍的物体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
