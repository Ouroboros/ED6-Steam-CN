import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1304_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1304   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1304.x'
    header.mapIndex       = 52
    header.bgm            = 89
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
        ('ED6_DT07/CH02073._CH', 'ED6_DT07/CH02073P._CP'),
        ('ED6_DT27/CH03573._CH', 'ED6_DT27/CH03573P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH00324._CH', 'ED6_DT07/CH00324P._CP'),
        ('ED6_DT06/CH20043._CH', 'ED6_DT06/CH20043P._CP'),
        ('ED6_DT27/CH03015._CH', 'ED6_DT27/CH03015P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '穆拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '料理',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524292,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '料理',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524292,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '投发烟筒的人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1310724,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '接发烟筒的人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1310724,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x24A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x24A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -56680,
            triggerZ            = 0,
            triggerY            = -43550,
            triggerRange        = 1000,
            actorX              = -57380,
            actorZ              = 0,
            actorY              = -43550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -52110,
            triggerZ            = 0,
            triggerY            = -41540,
            triggerRange        = 1000,
            actorX              = -52130,
            actorZ              = 0,
            actorY              = -40880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x292
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2A3',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_0C_D2F)

    Jump('loc_2C2')

    def _loc_2A3(): pass

    label('loc_2A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_2B4',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_04_5B5)

    Jump('loc_2C2')

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_2C2',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_05_6C3)

    def _loc_2C2(): pass

    label('loc_2C2')

    Return()

# id: 0x0001 offset: 0x2C3
@scena.Code('func_01_2C3')
def func_01_2C3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 2, 0x190A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D5',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2DC')

    def _loc_2D5(): pass

    label('loc_2D5')

    OP_6F(0x0003, 60)

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 3, 0x190B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EE',
    )

    OP_6F(0x0004, 0)

    Jump('loc_2F5')

    def _loc_2EE(): pass

    label('loc_2EE')

    OP_6F(0x0004, 60)

    def _loc_2F5(): pass

    label('loc_2F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 2, 0x1802)),
            Expr.Return,
        ),
        'loc_37C',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrSetPos(0x000B, -52060, 0, -95510, 135)
    ChrSetPos(0x000C, -49600, 0, -95370, 180)
    ChrSetPos(0x000D, -50540, 0, -96510, 0)
    ChrSetPos(0x000E, -50810, 0, -94450, 90)
    ChrSetChipByIndex(0x000B, 6)
    ChrSetChipByIndex(0x000C, 6)
    ChrSetChipByIndex(0x000D, 6)
    ChrSetChipByIndex(0x000E, 6)

    def _loc_37C(): pass

    label('loc_37C')

    Return()

# id: 0x0002 offset: 0x37D
@scena.Code('func_02_37D')
def func_02_37D():
    UnlockAchievement(0x02, 0x0048, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 2, 0x190A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['羽毛胸针'], 1)"),
            Expr.Return,
        ),
        'loc_3F1',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['羽毛胸针']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0321, 2, 0x190A))

    Jump('loc_457')

    def _loc_3F1(): pass

    label('loc_3F1')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['羽毛胸针']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['羽毛胸针']),
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

    def _loc_457(): pass

    label('loc_457')

    Jump('loc_48B')

    def _loc_45A(): pass

    label('loc_45A')

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
    def _loc_48B(): pass

    label('loc_48B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x499
@scena.Code('func_03_499')
def func_03_499():
    UnlockAchievement(0x02, 0x0049, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0321, 3, 0x190B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_576',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_50D',
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
    SetScenaFlags(ScenaFlag(0x0321, 3, 0x190B))

    Jump('loc_573')

    def _loc_50D(): pass

    label('loc_50D')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_573(): pass

    label('loc_573')

    Jump('loc_5A7')

    def _loc_576(): pass

    label('loc_576')

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
    def _loc_5A7(): pass

    label('loc_5A7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5B5
@scena.Code('func_04_5B5')
def func_04_5B5():
    EventBegin(0x00)
    CameraMove(-50630, 0, -95070, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x000B, -52060, 0, -95510, 90)
    ChrSetPos(0x000C, -49600, 0, -95370, 270)
    ChrSetPos(0x000D, -50540, 0, -96510, 0)
    ChrSetPos(0x000E, -50810, 0, -94450, 180)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#2450280190V#6P好了……\n',
            '差不多该换班了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2460280191V慢慢走出去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C1306._SN', 137, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x6C3
@scena.Code('func_05_6C3')
def func_05_6C3():
    EventBegin(0x00)
    CameraMove(-50630, 0, -95070, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x000B, -52060, 0, -95510, 90)
    ChrSetPos(0x000C, -49600, 0, -95370, 270)
    ChrSetPos(0x000D, -50540, 0, -96510, 0)
    ChrSetPos(0x000E, -50810, 0, -94450, 180)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    LoadEffect(0x00, 'map\\\\mp004_00.eff')
    ChrSetPos(0x0011, -51470, 0, -100000, 0)
    ChrSetPos(0x0012, -50830, 0, -95400, 0)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x0012, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#2500280196V嗯……？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x000C,
        (
            '#2460280197V什么……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    PlaySE(127, 0x00, 0x64)
    Sleep(300)

    OP_56(0x00)
    Sleep(300)

    CreateThread(0x000B, 0x01, 0x00, func_0B_CB3)
    Sleep(100)

    ChrTalk(
        0x000E,
        (
            '#2500280198V呜哇！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x000B,
        (
            '#2450280199V什……什么……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    FadeOut(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)

    OP_56(0x00)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#2460280200V不行了……\n',
            '……意识模糊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 135, 400)
    Sleep(600)

    ChrSetDirection(0x000C, 90, 400)
    CreateThread(0x000B, 0x01, 0x00, func_06_B60)
    Sleep(100)

    CreateThread(0x000C, 0x01, 0x00, func_06_B60)
    Sleep(200)

    CreateThread(0x000D, 0x01, 0x00, func_06_B60)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, func_06_B60)
    WaitForThreadExit(0x000E, 0x0001)
    ChrSetPos(0x000B, -52060, 0, -95510, 135)
    ChrSetPos(0x000C, -49600, 0, -95370, 180)
    ChrSetPos(0x000D, -50540, 0, -96510, 0)
    ChrSetPos(0x000E, -50810, 0, -94450, 90)
    ChrSetChipByIndex(0x000B, 6)
    ChrSetChipByIndex(0x000C, 6)
    ChrSetChipByIndex(0x000D, 6)
    ChrSetChipByIndex(0x000E, 6)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    CameraMove(-50470, 0, -97380, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    FadeIn(1000, 16777215)
    OP_0D()
    FadeIn(2000, 16777215)
    OP_0D()
    CreateThread(0x012A, 0x01, 0x00, func_0A_C64)
    Sleep(500)

    CreateThread(0x0146, 0x01, 0x00, func_09_C15)
    Sleep(500)

    CreateThread(0x0129, 0x01, 0x00, func_08_BC6)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_07_B7E)
    WaitForThreadExit(0x0146, 0x0001)

    ChrTalk(
        0x0146,
        (
            '#0090280201V#213F好、好惊人的威力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280202V#192FＳ２弹……是催眠瓦斯弹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012A, 0x0102, 400)

    ChrTalk(
        0x012A,
        (
            '#0290280203V#200F#5P看来比市面上那些卖的普通货\n',
            '即效性要强很多呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290280204V里面是自己调配的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020280205V#1035F#6P……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020280206V#1031F不过，这个调配法是商业机密。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012A,
        (
            '#0290280207V#206F#5P小气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0129,
        (
            '#0300280208V#490F算了。\n',
            '赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0300, 2, 0x1802))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xB60
@scena.Code('func_06_B60')
def func_06_B60():
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 5)
    OP_99(0x00FE, 0x00, 0x03, 1000)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 6)

    Return()

# id: 0x0007 offset: 0xB7E
@scena.Code('func_07_B7E')
def func_07_B7E():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -51090, 0, -101180, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0BA5')
    def lambda_0BA5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0BA5)

    ChrWalkTo(0x00FE, -51510, 0, -99340, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0xBC6
@scena.Code('func_08_BC6')
def func_08_BC6():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -51090, 0, -101180, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0BED')
    def lambda_0BED():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0BED)

    ChrWalkTo(0x00FE, -50310, 0, -99030, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0009 offset: 0xC15
@scena.Code('func_09_C15')
def func_09_C15():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -51090, 0, -101180, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0C3C')
    def lambda_0C3C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0C3C)

    ChrWalkTo(0x00FE, -51540, 0, -98050, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000A offset: 0xC64
@scena.Code('func_0A_C64')
def func_0A_C64():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -51090, 0, -101180, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_0C8B')
    def lambda_0C8B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0C8B)

    ChrWalkTo(0x00FE, -50350, 0, -97820, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000B offset: 0xCB3
@scena.Code('func_0B_CB3')
def func_0B_CB3():
    @scena.Lambda('lambda_0CB9')
    def lambda_0CB9():
        ChrMoveTo(0x00FE, -53000, 0, -95570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0CB9)

    Sleep(50)

    @scena.Lambda('lambda_0CD9')
    def lambda_0CD9():
        ChrMoveTo(0x00FE, -48570, 0, -95370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_0CD9)

    Sleep(50)

    @scena.Lambda('lambda_0CF9')
    def lambda_0CF9():
        ChrMoveTo(0x00FE, -50410, 0, -97550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0CF9)

    Sleep(50)

    @scena.Lambda('lambda_0D19')
    def lambda_0D19():
        ChrMoveTo(0x00FE, -51140, 0, -93600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0D19)

    Return()

# id: 0x000C offset: 0xD2F
@scena.Code('func_0C_D2F')
def func_0C_D2F():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x0009, 5360, 200, -92360, 192)
    ChrSetPos(0x0008, 4720, 200, -94810, 12)
    ChrSetPos(0x000A, 6630, 0, -93560, 270)
    ChrSetPos(0x000F, 5200, 850, -93300, 0)
    ChrSetPos(0x0010, 4760, 850, -94000, 0)
    CameraMove(5760, 0, -92560, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0280280209V#151F啊～竟然能在取材时\n',
            '受到这么丰盛的款待～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280210V朵洛希，实在太感动了～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2440280211V嘿嘿，你这么说\n',
            '我露这一手也算是值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2440280212V埃雷波尼亚帝国的先生，您觉得怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280213V#277F#5P啊啊……无可挑剔的美味。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280214V和帝国军的伙食相比\n',
            '真是天差地别啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2440280215V哦，是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2440280216V埃雷波尼亚军的士兵们\n',
            '都吃些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280217V#276F#5P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280218V#272F很咸的牛肉罐头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280219V煮烂了没味道的豆子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280220V发霉的黑面包。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280221V#270F这三样食物可以说\n',
            '是必备的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2440280222V呜哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280280223V#154F呜哇～好可怜哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280280224V每天都吃那样的东西，\n',
            '谁还想打仗啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280225V#276F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2440280226V哇哈哈。\n',
            '这位小姐说话真刻薄啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0110280227V#272F#5P我也希望\n',
            '没有这种事才好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280228V#270F只是，为了维持巨大的兵力，\n',
            '只能把粮食的质量抑制在最低限度……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110280229V这样的想法也确实存在的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0280280230V#153F呼～好可怜哦～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2440280231V你们也真是够辛苦的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C1305._SN', 133, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
