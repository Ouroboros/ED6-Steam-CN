import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
        ('ED6_DT09/CH10880._CH', 'ED6_DT09/CH10880P._CP'),
        ('ED6_DT09/CH10881._CH', 'ED6_DT09/CH10881P._CP'),
        ('ED6_DT09/CH11160._CH', 'ED6_DT09/CH11160P._CP'),
        ('ED6_DT09/CH11161._CH', 'ED6_DT09/CH11161P._CP'),
        ('ED6_DT09/CH10200._CH', 'ED6_DT09/CH10200P._CP'),
        ('ED6_DT09/CH10201._CH', 'ED6_DT09/CH10201P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
        ('ED6_DT29/CH12440._CH', 'ED6_DT29/CH12440P._CP'),
        ('ED6_DT29/CH12441._CH', 'ED6_DT29/CH12441P._CP'),
        ('ED6_DT29/CH12500._CH', 'ED6_DT29/CH12500P._CP'),
        ('ED6_DT29/CH13030._CH', 'ED6_DT29/CH13030P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = -134573,
            z                   = 3995,
            y                   = 87240,
            direction           = 315,
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
            name                = '',
            x                   = -148670,
            z                   = 4059,
            y                   = 108220,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
    )

# id: 0x10002 offset: 0x18A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -146390,
            z           = 2009,
            y           = 152190,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -148000,
            z           = 2090,
            y           = 136280,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -154200,
            z           = 1990,
            y           = 120790,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -154710,
            z           = 4070,
            y           = 99880,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00D1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -154180,
            z           = 4030,
            y           = 76310,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -162330,
            z           = 4019,
            y           = 46020,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -131150,
            z           = 2040,
            y           = 55190,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -151910,
            z           = 5910,
            y           = -11960,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00D1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -151260,
            z           = 4040,
            y           = 20370,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00CD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x286
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -134573,
            y           = 3500,
            z           = 87240,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = -157500,
            y           = 3000,
            z           = 105200,
            range       = -142800,
            dword_10    = 0x00001770,
            dword_14    = 0x0001B134,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10004 offset: 0x2C6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -158410,
            triggerZ            = 1970,
            triggerY            = 120220,
            triggerRange        = 1000,
            actorX              = -158970,
            actorZ              = 1970,
            actorY              = 120040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -124550,
            triggerZ            = 4019,
            triggerY            = 90450,
            triggerRange        = 1000,
            actorX              = -123890,
            actorZ              = 4019,
            actorY              = 90020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -156400,
            triggerZ            = 3930,
            triggerY            = 80510,
            triggerRange        = 1000,
            actorX              = -156750,
            actorZ              = 3930,
            actorY              = 81120,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -170750,
            triggerZ            = 5900,
            triggerY            = 3230,
            triggerRange        = 1000,
            actorX              = -171430,
            actorZ              = 5900,
            actorY              = 3350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -130810,
            triggerZ            = 4050,
            triggerY            = 21300,
            triggerRange        = 1000,
            actorX              = -130139,
            actorZ              = 4050,
            actorY              = 21690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x37A
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x37B
@scena.Code('func_01_37B')
def func_01_37B():
    OP_16(0x02, 4000, -267000, -56000, 2293822)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 0, 0x1B70)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39F',
    )

    OP_6F(0x0000, 0)

    Jump('loc_3A6')

    def _loc_39F(): pass

    label('loc_39F')

    OP_6F(0x0000, 60)

    def _loc_3A6(): pass

    label('loc_3A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 1, 0x1B71)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B8',
    )

    OP_6F(0x0001, 0)

    Jump('loc_3BF')

    def _loc_3B8(): pass

    label('loc_3B8')

    OP_6F(0x0001, 60)

    def _loc_3BF(): pass

    label('loc_3BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 2, 0x1B72)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D1',
    )

    OP_6F(0x0002, 0)

    Jump('loc_3D8')

    def _loc_3D1(): pass

    label('loc_3D1')

    OP_6F(0x0002, 60)

    def _loc_3D8(): pass

    label('loc_3D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 3, 0x1B73)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EA',
    )

    OP_6F(0x0003, 0)

    Jump('loc_3F1')

    def _loc_3EA(): pass

    label('loc_3EA')

    OP_6F(0x0003, 60)

    def _loc_3F1(): pass

    label('loc_3F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 4, 0x1B74)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_403',
    )

    OP_6F(0x0004, 0)

    Jump('loc_40A')

    def _loc_403(): pass

    label('loc_403')

    OP_6F(0x0004, 60)

    def _loc_40A(): pass

    label('loc_40A')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 6, 0x1A0E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43B',
    )

    ChrClearFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_43B(): pass

    label('loc_43B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_46A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_455',
    )

    ChrSetDirection(0x0009, 180, 0)

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041E, 6, 0x20F6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_467',
    )

    ChrClearFlags(0x0009, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_467(): pass

    label('loc_467')

    Jump('loc_474')

    def _loc_46A(): pass

    label('loc_46A')

    ChrSetFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    def _loc_474(): pass

    label('loc_474')

    Return()

# id: 0x0002 offset: 0x475
@scena.Code('func_02_475')
def func_02_475():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_48A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_475')

    def _loc_48A(): pass

    label('loc_48A')

    Return()

# id: 0x0003 offset: 0x48B
@scena.Code('func_03_48B')
def func_03_48B():
    UnlockAchievement(0x02, 0x0055, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 0, 0x1B70)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_568',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_4FF',
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
    SetScenaFlags(ScenaFlag(0x036E, 0, 0x1B70))

    Jump('loc_565')

    def _loc_4FF(): pass

    label('loc_4FF')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_565(): pass

    label('loc_565')

    Jump('loc_599')

    def _loc_568(): pass

    label('loc_568')

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
    def _loc_599(): pass

    label('loc_599')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5A7
@scena.Code('func_04_5A7')
def func_04_5A7():
    UnlockAchievement(0x02, 0x0056, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 1, 0x1B71)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_684',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_61B',
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
    SetScenaFlags(ScenaFlag(0x036E, 1, 0x1B71))

    Jump('loc_681')

    def _loc_61B(): pass

    label('loc_61B')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_681(): pass

    label('loc_681')

    Jump('loc_6B5')

    def _loc_684(): pass

    label('loc_684')

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
    def _loc_6B5(): pass

    label('loc_6B5')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x6C3
@scena.Code('func_05_6C3')
def func_05_6C3():
    UnlockAchievement(0x02, 0x0057, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 2, 0x1B72)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_737',
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
    SetScenaFlags(ScenaFlag(0x036E, 2, 0x1B72))

    Jump('loc_79D')

    def _loc_737(): pass

    label('loc_737')

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

    def _loc_79D(): pass

    label('loc_79D')

    Jump('loc_7D1')

    def _loc_7A0(): pass

    label('loc_7A0')

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
    def _loc_7D1(): pass

    label('loc_7D1')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x7DF
@scena.Code('func_06_7DF')
def func_06_7DF():
    UnlockAchievement(0x02, 0x0058, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 3, 0x1B73)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8BC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_853',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x036E, 3, 0x1B73))

    Jump('loc_8B9')

    def _loc_853(): pass

    label('loc_853')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
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

    def _loc_8B9(): pass

    label('loc_8B9')

    Jump('loc_8ED')

    def _loc_8BC(): pass

    label('loc_8BC')

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
    def _loc_8ED(): pass

    label('loc_8ED')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x8FB
@scena.Code('func_07_8FB')
def func_07_8FB():
    UnlockAchievement(0x02, 0x0059, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036E, 4, 0x1B74)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_979',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 30)
    OP_73(0x0004)
    OP_6F(0x0004, 30)
    AddSepith(0x00, 200)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x036E, 4, 0x1B74))

    Jump('loc_993')

    def _loc_979(): pass

    label('loc_979')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_993(): pass

    label('loc_993')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x9A5
@scena.Code('func_08_9A5')
def func_08_9A5():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_9B5'),
        (0x00000065, 'loc_B07'),
        (-1, 'loc_C59'),
    )

    def _loc_9B5(): pass

    label('loc_9B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041E, 6, 0x20F6)),
            Expr.Return,
        ),
        'loc_9BD',
    )

    Return()

    def _loc_9BD(): pass

    label('loc_9BD')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_AA2'),
        (-1, 'loc_AC5'),
    )

    def _loc_AA2(): pass

    label('loc_AA2')

    Fade(500)
    OP_89(0x0000, -148540, 2360, 114080, 156)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_AC5(): pass

    label('loc_AC5')

    Battle(0x00000EED, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -148540, 2360, 114080, 156)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_AFE'),
        (0x00000001, 'loc_B01'),
        (-1, 'loc_B04'),
    )

    def _loc_AFE(): pass

    label('loc_AFE')

    EventEnd(0x00)

    Return()

    def _loc_B01(): pass

    label('loc_B01')

    OP_B4(0x00)

    Return()

    def _loc_B04(): pass

    label('loc_B04')

    Jump('loc_C59')

    def _loc_B07(): pass

    label('loc_B07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041E, 6, 0x20F6)),
            Expr.Return,
        ),
        'loc_B0F',
    )

    Return()

    def _loc_B0F(): pass

    label('loc_B0F')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_BF4'),
        (-1, 'loc_C17'),
    )

    def _loc_BF4(): pass

    label('loc_BF4')

    Fade(500)
    OP_89(0x0000, -148760, 3940, 101000, 18)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_C17(): pass

    label('loc_C17')

    Battle(0x00000EF7, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -148760, 3940, 101000, 18)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_C50'),
        (0x00000001, 'loc_C53'),
        (-1, 'loc_C56'),
    )

    def _loc_C50(): pass

    label('loc_C50')

    EventEnd(0x00)

    Return()

    def _loc_C53(): pass

    label('loc_C53')

    OP_B4(0x00)

    Return()

    def _loc_C56(): pass

    label('loc_C56')

    Jump('loc_C59')

    def _loc_C59(): pass

    label('loc_C59')

    EventBegin(0x01)
    ChrSetFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x041E, 6, 0x20F6))
    OP_28(0x00B5, 0x04, 0x10)
    OP_28(0x00B5, 0x04, 0x02)
    OP_28(0x00B5, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0xCC5
@scena.Code('func_09_CC5')
def func_09_CC5():
    EventBegin(0x01)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000000, 'loc_D2E'),
        (0x00000001, 'loc_F5E'),
        (-1, 'loc_FC6'),
    )

    def _loc_D2E(): pass

    label('loc_D2E')

    Battle(0x000000D3, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_D4F'),
        (0x00000002, 'loc_EDE'),
        (0x00000001, 'loc_F56'),
        (-1, 'loc_F5B'),
    )

    def _loc_D4F(): pass

    label('loc_D4F')

    EventBegin(0x01)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DF0',
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
        0,
        (
            TXT(0x00, '【◇消灭了琥珀之塔和迷雾峡谷的通缉魔兽】\n'),
            TXT(0x01, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_DDB'),
        (-1, 'loc_DF0'),
    )

    def _loc_DDB(): pass

    label('loc_DDB')

    SetScenaFlags(ScenaFlag(0x0341, 7, 0x1A0F))
    SetScenaFlags(ScenaFlag(0x0342, 0, 0x1A10))
    OP_28(0x00B2, 0x01, 0x0001)
    OP_28(0x00B3, 0x01, 0x0001)

    Jump('loc_DF0')

    def _loc_DF0(): pass

    label('loc_DF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 7, 0x1A0F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 0, 0x1A10)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E02',
    )

    Call(0, 0x000A)

    Jump('loc_EDB')

    def _loc_E02(): pass

    label('loc_E02')

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetPos(0x0000, -136150, 4030, 88170, 135)
    ChrSetPos(0x0001, -136150, 4030, 88170, 135)
    ChrSetPos(0x0002, -136150, 4030, 88170, 135)
    ChrSetPos(0x0003, -136150, 4030, 88170, 135)
    OP_69(0x0000, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了古罗尼山顶的通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    OP_28(0x00B1, 0x01, 0x0001)
    OP_28(0x0093, 0x02, 0x0002)
    OP_28(0x0093, 0x01, 0x0004)
    OP_28(0x0093, 0x01, 0x0008)
    Sleep(400)

    def _loc_EDB(): pass

    label('loc_EDB')

    Jump('loc_F5B')

    def _loc_EDE(): pass

    label('loc_EDE')

    EventBegin(0x01)
    FadeOut(0, 0, -1)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetPos(0x0000, -138230, 4019, 89590, 135)
    ChrSetPos(0x0001, -138230, 4019, 89590, 135)
    ChrSetPos(0x0002, -138230, 4019, 89590, 135)
    ChrSetPos(0x0003, -138230, 4019, 89590, 135)
    OP_69(0x0000, 0)
    FadeIn(1000, 0)
    OP_0D()

    Jump('loc_F5B')

    def _loc_F56(): pass

    label('loc_F56')

    OP_B4(0x00)

    Jump('loc_F5B')

    def _loc_F5B(): pass

    label('loc_F5B')

    Jump('loc_FC6')

    def _loc_F5E(): pass

    label('loc_F5E')

    Fade(500)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetPos(0x0000, -138230, 4019, 89590, 135)
    ChrSetPos(0x0001, -138230, 4019, 89590, 135)
    ChrSetPos(0x0002, -138230, 4019, 89590, 135)
    ChrSetPos(0x0003, -138230, 4019, 89590, 135)
    OP_69(0x0000, 0)
    OP_0D()

    Jump('loc_FC6')

    def _loc_FC6(): pass

    label('loc_FC6')

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0xFC9
@scena.Code('func_0A_FC9')
def func_0A_FC9():
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
        'loc_FDC',
    )

    Call(0, 0x000B)

    def _loc_FDC(): pass

    label('loc_FDC')

    CameraMove(-135710, 4050, 87980, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(260000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -136610, 4010, 88580, 135)
    ChrSetPos(0x0106, -136320, 4010, 87160, 45)
    ChrSetPos(0x00F8, -134790, 4030, 89020, 225)
    ChrSetPos(0x00F9, -134630, 4000, 87460, 315)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010300715V#1007F哈～总算是解决了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300716V#1002F不过……\n',
            '这些魔兽的样子似乎很奇怪啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '是哪里和平时不同了呢？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【魔兽变强了】\n'),
            TXT(0x01, '【魔兽变胆怯了】\n'),
            TXT(0x02, '【魔兽非常兴奋】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1182'),
        (0x00000001, 'loc_13BB'),
        (0x00000002, 'loc_15CE'),
        (-1, 'loc_17E1'),
    )

    def _loc_1182(): pass

    label('loc_1182')

    OP_2B(0x0093, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_120F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300717V#072F那也没错……\n',
            '不过更明显的是它们的性情变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B2')

    def _loc_120F(): pass

    label('loc_120F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_129D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300719V#022F那也说的没错……\n',
            '不过更明显的是它们的性情变了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B2')

    def _loc_129D(): pass

    label('loc_129D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_132D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300721V#032F嗯、那也说的不错，\n',
            '不过更明显的是它们的性情变了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B2')

    def _loc_132D(): pass

    label('loc_132D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13B2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300723V#043F那样说也对，\n',
            '不过更明显的是它们的性情变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13B2(): pass

    label('loc_13B2')

    OP_28(0x0093, 0x01, 0x0400)

    Jump('loc_17E1')

    def _loc_13BB(): pass

    label('loc_13BB')

    OP_2B(0x0093, 0x0003)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1444',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300725V#072F啊啊～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C5')

    def _loc_1444(): pass

    label('loc_1444')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14C6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300727V#022F哎～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C5')

    def _loc_14C6(): pass

    label('loc_14C6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1546',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300729V#032F嗯，哪个地方的魔兽\n',
            '都好像很奇怪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C5')

    def _loc_1546(): pass

    label('loc_1546')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15C5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300731V#042F是啊，不管什么样的魔兽\n',
            '也都很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15C5(): pass

    label('loc_15C5')

    OP_28(0x0093, 0x01, 0x1000)

    Jump('loc_17E1')

    def _loc_15CE(): pass

    label('loc_15CE')

    OP_2B(0x0093, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1657',
    )

    ChrTalk(
        0x0108,
        (
            '#0080300725V#072F啊啊～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300718V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D8')

    def _loc_1657(): pass

    label('loc_1657')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16D9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300727V#022F哎～不管什么样的魔兽\n',
            '都变得很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300720V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D8')

    def _loc_16D9(): pass

    label('loc_16D9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1759',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300729V#032F嗯，哪个地方的魔兽\n',
            '都好像很奇怪啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300722V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D8')

    def _loc_1759(): pass

    label('loc_1759')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17D8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300731V#042F是啊，不管什么样的魔兽\n',
            '也都很奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300724V变得异常地凶暴，\n',
            '陷入了某种恐慌之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D8(): pass

    label('loc_17D8')

    OP_28(0x0093, 0x01, 0x0800)

    Jump('loc_17E1')

    def _loc_17E1(): pass

    label('loc_17E1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1841',
    )

    ChrTalk(
        0x0107,
        (
            '#0070300741V#065F我、我也\n',
            '有那种感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300742V#561F好、好可怕啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_195E')

    def _loc_1841(): pass

    label('loc_1841')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18A0',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300743V#043F我也……\n',
            '有那种感觉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300744V究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_195E')

    def _loc_18A0(): pass

    label('loc_18A0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18FF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300745V#032F我也有\n',
            '同样的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300746V嗯，到底是为什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_195E')

    def _loc_18FF(): pass

    label('loc_18FF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_195E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300747V#026F我也有同感啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300748V#522F嗯……\n',
            '究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_195E(): pass

    label('loc_195E')

    ChrTalk(
        0x0106,
        (
            '#0050300749V#057F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300750V#1004F嗯？　怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300751V#555F啊，没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300752V或许这是\n',
            '某种前兆也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300753V#1020F前兆……\n',
            '难道是『结社』！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300754V#552F那就不知道了……\n',
            '不过以前也发生过类似的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300755V魔兽突然就变得\n',
            '仓惶不安…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300756V之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300757V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300758V#1004F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B2C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070300759V#063F阿加特哥哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B2C(): pass

    label('loc_1B2C')

    ChrTalk(
        0x0106,
        (
            '#0050300760V#053F算了，今天就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300761V#057F不管怎么说，动物的直觉\n',
            '有时候比人更敏锐的，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300762V我们也必须准备应付\n',
            '随时可能出现的特殊情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300763V#1002F嗯……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300764V那么…\n',
            '我们暂时先返回协会吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300765V#050F啊啊～就这样办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0341, 6, 0x1A0E))
    OP_28(0x00B1, 0x01, 0x0001)
    OP_28(0x0093, 0x02, 0x0002)
    OP_28(0x0093, 0x01, 0x0004)
    OP_28(0x0093, 0x01, 0x0008)
    OP_28(0x0093, 0x01, 0x2000)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x1C6E
@scena.Code('func_0B_1C6E')
def func_0B_1C6E():
    FadeOut(0, 0, -1)
    CameraMove(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_1D25'),
        (0x00000001, 'loc_1D2B'),
        (-1, 'loc_1D31'),
    )

    def _loc_1D25(): pass

    label('loc_1D25')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1D31')

    def _loc_1D2B(): pass

    label('loc_1D2B')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1D31')

    def _loc_1D31(): pass

    label('loc_1D31')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
