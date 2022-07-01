import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3601_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3601   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3601.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x136D
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
        ('ED6_DT29/CH12660._CH', 'ED6_DT29/CH12660P._CP'),
        ('ED6_DT29/CH12661._CH', 'ED6_DT29/CH12661P._CP'),
        ('ED6_DT29/CH12670._CH', 'ED6_DT29/CH12670P._CP'),
        ('ED6_DT29/CH12671._CH', 'ED6_DT29/CH12671P._CP'),
        ('ED6_DT29/CH12680._CH', 'ED6_DT29/CH12680P._CP'),
        ('ED6_DT29/CH12681._CH', 'ED6_DT29/CH12681P._CP'),
        ('ED6_DT29/CH12690._CH', 'ED6_DT29/CH12690P._CP'),
        ('ED6_DT29/CH12691._CH', 'ED6_DT29/CH12691P._CP'),
        ('ED6_DT29/CH12700._CH', 'ED6_DT29/CH12700P._CP'),
        ('ED6_DT29/CH12701._CH', 'ED6_DT29/CH12701P._CP'),
        ('ED6_DT29/CH12710._CH', 'ED6_DT29/CH12710P._CP'),
        ('ED6_DT29/CH12711._CH', 'ED6_DT29/CH12711P._CP'),
        ('ED6_DT29/CH12720._CH', 'ED6_DT29/CH12720P._CP'),
        ('ED6_DT29/CH12721._CH', 'ED6_DT29/CH12721P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -20,
            z                   = 1000,
            y                   = -31930,
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

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 18090,
            z           = 4400,
            y           = 14060,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1EB5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 1910,
            z           = 4400,
            y           = -18170,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EB6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 33620,
            z           = 400,
            y           = 17700,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1EB7,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x18E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x18E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 18030,
            triggerZ            = 4400,
            triggerY            = 7080,
            triggerRange        = 1000,
            actorX              = 18030,
            actorZ              = 4400,
            actorY              = 6460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12960,
            triggerZ            = -3600,
            triggerY            = 18020,
            triggerRange        = 1000,
            actorX              = 12260,
            actorZ              = -3600,
            actorY              = 18010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20,
            triggerZ            = -50,
            triggerY            = -31270,
            triggerRange        = 1000,
            actorX              = -20,
            actorZ              = -50,
            actorY              = -31930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6850,
            triggerZ            = 400,
            triggerY            = -31890,
            triggerRange        = 1000,
            actorX              = 7560,
            actorZ              = 400,
            actorY              = -31890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20,
            triggerZ            = 400,
            triggerY            = -38890,
            triggerRange        = 1000,
            actorX              = -20,
            actorZ              = 400,
            actorY              = -39510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -6950,
            triggerZ            = 400,
            triggerY            = -31950,
            triggerRange        = 1000,
            actorX              = -7610,
            actorZ              = 400,
            actorY              = -31950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x266
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_27E'),
        (0x00000065, 'loc_285'),
        (0x00000066, 'loc_28C'),
        (0x00000067, 'loc_293'),
        (-1, 'loc_29A'),
    )

    def _loc_27E(): pass

    label('loc_27E')

    Event(0, 0x0009)

    Jump('loc_29A')

    def _loc_285(): pass

    label('loc_285')

    Event(0, 0x000B)

    Jump('loc_29A')

    def _loc_28C(): pass

    label('loc_28C')

    Event(0, 0x000D)

    Jump('loc_29A')

    def _loc_293(): pass

    label('loc_293')

    Event(0, 0x000F)

    Jump('loc_29A')

    def _loc_29A(): pass

    label('loc_29A')

    Return()

# id: 0x0001 offset: 0x29B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 0, 0x1F30)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AD',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2B4')

    def _loc_2AD(): pass

    label('loc_2AD')

    OP_6F(0x0000, 60)

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 1, 0x1F31)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C6',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2CD')

    def _loc_2C6(): pass

    label('loc_2C6')

    OP_6F(0x0001, 60)

    def _loc_2CD(): pass

    label('loc_2CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 2, 0x1F32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2E6')

    def _loc_2DF(): pass

    label('loc_2DF')

    OP_6F(0x0002, 60)

    def _loc_2E6(): pass

    label('loc_2E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 4, 0x1F34)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F8',
    )

    OP_6F(0x0003, 0)

    Jump('loc_2FF')

    def _loc_2F8(): pass

    label('loc_2F8')

    OP_6F(0x0003, 60)

    def _loc_2FF(): pass

    label('loc_2FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 5, 0x1F35)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_311',
    )

    OP_6F(0x0004, 0)

    Jump('loc_318')

    def _loc_311(): pass

    label('loc_311')

    OP_6F(0x0004, 60)

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 6, 0x1F36)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32A',
    )

    OP_6F(0x0005, 0)

    Jump('loc_331')

    def _loc_32A(): pass

    label('loc_32A')

    OP_6F(0x0005, 60)

    def _loc_331(): pass

    label('loc_331')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 5, 0x1EB5)),
            Expr.Return,
        ),
        'loc_365',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_365(): pass

    label('loc_365')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 6, 0x1EB6)),
            Expr.Return,
        ),
        'loc_371',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_371(): pass

    label('loc_371')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D6, 7, 0x1EB7)),
            Expr.Return,
        ),
        'loc_37D',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_37D(): pass

    label('loc_37D')

    OP_1B(0x00, 0x00, 0x000A)
    OP_1B(0x01, 0x00, 0x000C)
    OP_1B(0x02, 0x00, 0x000E)
    OP_1B(0x03, 0x00, 0x0010)

    Return()

# id: 0x0002 offset: 0x392
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_3A7(): pass

    label('loc_3A7')

    Return()

# id: 0x0003 offset: 0x3A8
@scena.Code('func_03_3A8')
def func_03_3A8():
    UnlockAchievement(0x02, 0xDC, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 0, 0x1F30)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_485',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_41C',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F30)

    Jump('loc_482')

    def _loc_41C(): pass

    label('loc_41C')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_482(): pass

    label('loc_482')

    Jump('loc_4B6')

    def _loc_485(): pass

    label('loc_485')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_4B6(): pass

    label('loc_4B6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4C4
@scena.Code('func_04_4C4')
def func_04_4C4():
    UnlockAchievement(0x02, 0xDD, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 1, 0x1F31)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A1',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_538',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F31)

    Jump('loc_59E')

    def _loc_538(): pass

    label('loc_538')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_59E(): pass

    label('loc_59E')

    Jump('loc_5D2')

    def _loc_5A1(): pass

    label('loc_5A1')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_5D2(): pass

    label('loc_5D2')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5E0
@scena.Code('func_05_5E0')
def func_05_5E0():
    UnlockAchievement(0x02, 0xDE, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 2, 0x1F32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_778',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 3, 0x1F33)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C4',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0637')
    def lambda_0637():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0637)

    @scena.Lambda('lambda_0652')
    def lambda_0652():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0652)

    ClearChrFlags(0x0008, 0x0080)

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
    Battle(0x00000418, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_69F'),
        (0x00000002, 'loc_6B1'),
        (0x00000001, 'loc_6C1'),
        (-1, 'loc_6C4'),
    )

    def _loc_69F(): pass

    label('loc_69F')

    OP_A2(0x1F33)
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_6C4')

    def _loc_6B1(): pass

    label('loc_6B1')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_6C1(): pass

    label('loc_6C1')

    OP_B4(0x00)

    Return()

    def _loc_6C4(): pass

    label('loc_6C4')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['红耀石护符'], 1)"),
            Expr.Return,
        ),
        'loc_713',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['红耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F32)

    Jump('loc_775')

    def _loc_713(): pass

    label('loc_713')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['红耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['红耀石护符']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_775(): pass

    label('loc_775')

    Jump('loc_7A7')

    def _loc_778(): pass

    label('loc_778')

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
    def _loc_7A7(): pass

    label('loc_7A7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x7B5
@scena.Code('func_06_7B5')
def func_06_7B5():
    UnlockAchievement(0x02, 0xDF, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 4, 0x1F34)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_892',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_829',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F34)

    Jump('loc_88F')

    def _loc_829(): pass

    label('loc_829')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_88F(): pass

    label('loc_88F')

    Jump('loc_8C3')

    def _loc_892(): pass

    label('loc_892')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_8C3(): pass

    label('loc_8C3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x8D1
@scena.Code('func_07_8D1')
def func_07_8D1():
    UnlockAchievement(0x02, 0xE0, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 5, 0x1F35)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9AE',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_945',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F35)

    Jump('loc_9AB')

    def _loc_945(): pass

    label('loc_945')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_9AB(): pass

    label('loc_9AB')

    Jump('loc_9DF')

    def _loc_9AE(): pass

    label('loc_9AE')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_9DF(): pass

    label('loc_9DF')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x9ED
@scena.Code('func_08_9ED')
def func_08_9ED():
    UnlockAchievement(0x02, 0xE1, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E6, 6, 0x1F36)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ACA',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['活性之药'], 1)"),
            Expr.Return,
        ),
        'loc_A61',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F36)

    Jump('loc_AC7')

    def _loc_A61(): pass

    label('loc_A61')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_AC7(): pass

    label('loc_AC7')

    Jump('loc_AFB')

    def _loc_ACA(): pass

    label('loc_ACA')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_AFB(): pass

    label('loc_AFB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xB09
@scena.Code('func_09_B09')
def func_09_B09():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 190, 34280, 0)
    SetChrPos(0x0101, 500, 190, 33780, 180)
    SetChrPos(0x0102, -500, 190, 33780, 180)
    SetChrPos(0x00F8, 500, 190, 34780, 180)
    SetChrPos(0x00F9, -500, 190, 34780, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0011)
    Call(0, 0x0013)
    Fade(500)
    OP_6D(-90, 190, 32189, 0)
    SetChrPos(0x0000, -90, 190, 32189, 180)
    SetChrPos(0x0001, -90, 190, 32189, 180)
    SetChrPos(0x0002, -90, 190, 32189, 180)
    SetChrPos(0x0003, -90, 190, 32189, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000A offset: 0xC09
@scena.Code('func_0A_C09')
def func_0A_C09():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, 190, 34280, 0)
    SetChrPos(0x0101, -500, 190, 34780, 0)
    SetChrPos(0x0102, 500, 190, 34780, 0)
    SetChrPos(0x00F8, -500, 190, 33780, 0)
    SetChrPos(0x00F9, 500, 190, 33780, 0)
    OP_0D()
    Call(0, 0x0011)
    Call(0, 0x0014)
    NewScene('ED6_DT21/C3600._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0xC81
@scena.Code('func_0B_C81')
def func_0B_C81():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(34000, 190, 630, 0)
    SetChrPos(0x0101, 34500, 190, 130, 180)
    SetChrPos(0x0102, 33500, 190, 130, 180)
    SetChrPos(0x00F8, 34500, 190, 1130, 180)
    SetChrPos(0x00F9, 33500, 190, 1130, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0012)
    Call(0, 0x0013)
    Fade(500)
    OP_6D(34000, 190, -1740, 0)
    SetChrPos(0x0000, 34000, 190, -1740, 180)
    SetChrPos(0x0001, 34000, 190, -1740, 180)
    SetChrPos(0x0002, 34000, 190, -1740, 180)
    SetChrPos(0x0003, 34000, 190, -1740, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000C offset: 0xD81
@scena.Code('func_0C_D81')
def func_0C_D81():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(34000, 190, 630, 0)
    SetChrPos(0x0101, 33500, 190, 1130, 0)
    SetChrPos(0x0102, 34500, 190, 1130, 0)
    SetChrPos(0x00F8, 33500, 190, 130, 0)
    SetChrPos(0x00F9, 34500, 190, 130, 0)
    OP_0D()
    Call(0, 0x0012)
    Call(0, 0x0014)
    NewScene('ED6_DT21/C3602._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0xDF9
@scena.Code('func_0D_DF9')
def func_0D_DF9():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 190, 500, 0)
    SetChrPos(0x0101, 500, 190, 0, 180)
    SetChrPos(0x0102, -500, 190, 0, 180)
    SetChrPos(0x00F8, 500, 190, 1000, 180)
    SetChrPos(0x00F9, -500, 190, 1000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0012)
    Call(0, 0x0013)
    Fade(500)
    OP_6D(130, 190, -1790, 0)
    SetChrPos(0x0000, 130, 190, -1790, 180)
    SetChrPos(0x0001, 130, 190, -1790, 180)
    SetChrPos(0x0002, 130, 190, -1790, 180)
    SetChrPos(0x0003, 130, 190, -1790, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000E offset: 0xEF9
@scena.Code('func_0E_EF9')
def func_0E_EF9():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, 190, 500, 0)
    SetChrPos(0x0101, -500, 190, 1000, 0)
    SetChrPos(0x0102, 500, 190, 1000, 0)
    SetChrPos(0x00F8, -500, 190, 0, 0)
    SetChrPos(0x00F9, 500, 190, 0, 0)
    OP_0D()
    Call(0, 0x0012)
    Call(0, 0x0014)
    NewScene('ED6_DT21/C3602._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0xF71
@scena.Code('func_0F_F71')
def func_0F_F71():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-34000, 190, 500, 0)
    SetChrPos(0x0101, -33500, 190, 0, 180)
    SetChrPos(0x0102, -34500, 190, 0, 180)
    SetChrPos(0x00F8, -33500, 190, 1000, 180)
    SetChrPos(0x00F9, -34500, 190, 1000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0012)
    Call(0, 0x0013)
    Fade(500)
    OP_6D(-33710, 190, -1710, 0)
    SetChrPos(0x0000, -33710, 190, -1710, 180)
    SetChrPos(0x0001, -33710, 190, -1710, 180)
    SetChrPos(0x0002, -33710, 190, -1710, 180)
    SetChrPos(0x0003, -33710, 190, -1710, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0010 offset: 0x1071
@scena.Code('func_10_1071')
def func_10_1071():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(-34000, 190, 500, 0)
    SetChrPos(0x0101, -34500, 190, 1000, 0)
    SetChrPos(0x0102, -33500, 190, 1000, 0)
    SetChrPos(0x00F8, -34500, 190, 0, 0)
    SetChrPos(0x00F9, -33500, 190, 0, 0)
    OP_0D()
    Call(0, 0x0012)
    Call(0, 0x0014)
    NewScene('ED6_DT21/C3602._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x10E9
@scena.Code('func_11_10E9')
def func_11_10E9():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0012 offset: 0x11C8
@scena.Code('func_12_11C8')
def func_12_11C8():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0013 offset: 0x12A7
@scena.Code('func_13_12A7')
def func_13_12A7():
    @scena.Lambda('lambda_12AD')
    def lambda_12AD():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_12AD)

    @scena.Lambda('lambda_12BF')
    def lambda_12BF():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_12BF)

    @scena.Lambda('lambda_12D1')
    def lambda_12D1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_12D1)

    @scena.Lambda('lambda_12E3')
    def lambda_12E3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_12E3)

    Sleep(2500)

    Return()

# id: 0x0014 offset: 0x12F5
@scena.Code('func_14_12F5')
def func_14_12F5():
    @scena.Lambda('lambda_12FB')
    def lambda_12FB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_12FB)

    @scena.Lambda('lambda_130D')
    def lambda_130D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_130D)

    @scena.Lambda('lambda_131F')
    def lambda_131F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_131F)

    @scena.Lambda('lambda_1331')
    def lambda_1331():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1331)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
