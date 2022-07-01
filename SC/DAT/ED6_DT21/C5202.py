import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5202   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5202.x'
    header.mapIndex       = 1
    header.bgm            = 63
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x822
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
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 9910,
            z                   = -3000,
            y                   = 271990,
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
            x           = 7140,
            z           = 0,
            y           = 78500,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0440,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -10,
            z           = 0,
            y           = 173660,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0442,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 20,
            z           = 0,
            y           = 271220,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0441,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -188060,
            z           = 0,
            y           = 155810,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0443,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -190000,
            z           = -4000,
            y           = 174020,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0442,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 18010,
            z           = 0,
            y           = 369940,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0441,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14480,
            z           = 0,
            y           = 383370,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0444,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 14180,
            z           = 0,
            y           = 384030,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0440,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1FA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9290,
            triggerZ            = -4000,
            triggerY            = 271990,
            triggerRange        = 1000,
            actorX              = 9910,
            actorZ              = -4000,
            actorY              = 271990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2029,
            triggerZ            = 0,
            triggerY            = 449750,
            triggerRange        = 1000,
            actorX              = -2029,
            actorZ              = 0,
            actorY              = 450360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 990,
            triggerZ            = 0,
            triggerY            = 449750,
            triggerRange        = 1000,
            actorX              = 990,
            actorZ              = 0,
            actorY              = 450410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4030,
            triggerZ            = 0,
            triggerY            = 449750,
            triggerRange        = 1000,
            actorX              = 4030,
            actorZ              = 0,
            actorY              = 450370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x28A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x28B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 3, 0x2313)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29D',
    )

    OP_6F(0x0008, 0)

    Jump('loc_2A4')

    def _loc_29D(): pass

    label('loc_29D')

    OP_6F(0x0008, 60)

    def _loc_2A4(): pass

    label('loc_2A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 5, 0x2315)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B6',
    )

    OP_6F(0x0009, 0)

    Jump('loc_2BD')

    def _loc_2B6(): pass

    label('loc_2B6')

    OP_6F(0x0009, 60)

    def _loc_2BD(): pass

    label('loc_2BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 6, 0x2316)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CF',
    )

    OP_6F(0x000A, 0)

    Jump('loc_2D6')

    def _loc_2CF(): pass

    label('loc_2CF')

    OP_6F(0x000A, 60)

    def _loc_2D6(): pass

    label('loc_2D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 7, 0x2317)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E8',
    )

    OP_6F(0x000B, 0)

    Jump('loc_2EF')

    def _loc_2E8(): pass

    label('loc_2E8')

    OP_6F(0x000B, 60)

    def _loc_2EF(): pass

    label('loc_2EF')

    Return()

# id: 0x0002 offset: 0x2F0
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_305',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_305(): pass

    label('loc_305')

    Return()

# id: 0x0003 offset: 0x306
@scena.Code('func_03_306')
def func_03_306():
    UnlockAchievement(0x02, 0x12, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 3, 0x2313)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0008, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 4, 0x2314)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EA',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_035D')
    def lambda_035D():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_035D)

    @scena.Lambda('lambda_0378')
    def lambda_0378():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0378)

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
    Battle(0x00000447, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_3C5'),
        (0x00000002, 'loc_3D7'),
        (0x00000001, 'loc_3E7'),
        (-1, 'loc_3EA'),
    )

    def _loc_3C5(): pass

    label('loc_3C5')

    OP_A2(0x2314)
    OP_6F(0x0008, 60)
    Sleep(500)

    Jump('loc_3EA')

    def _loc_3D7(): pass

    label('loc_3D7')

    OP_6F(0x0008, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_3E7(): pass

    label('loc_3E7')

    OP_B4(0x00)

    Return()

    def _loc_3EA(): pass

    label('loc_3EA')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['赫耳墨斯神靴'], 1)"),
            Expr.Return,
        ),
        'loc_439',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['赫耳墨斯神靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x2313)

    Jump('loc_49B')

    def _loc_439(): pass

    label('loc_439')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['赫耳墨斯神靴']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['赫耳墨斯神靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0x00000000)

    def _loc_49B(): pass

    label('loc_49B')

    Jump('loc_4CD')

    def _loc_49E(): pass

    label('loc_49E')

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
    def _loc_4CD(): pass

    label('loc_4CD')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4DB
@scena.Code('func_04_4DB')
def func_04_4DB():
    UnlockAchievement(0x02, 0x13, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 5, 0x2315)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B0',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0009, 0x0000001E)
    OP_73(0x0009)
    OP_6F(0x0009, 30)
    AddSepith(0x00, 0x0064)
    AddSepith(0x01, 0x0064)
    AddSepith(0x02, 0x0064)
    AddSepith(0x03, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
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
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2315)

    Jump('loc_5CA')

    def _loc_5B0(): pass

    label('loc_5B0')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5CA(): pass

    label('loc_5CA')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5DC
@scena.Code('func_05_5DC')
def func_05_5DC():
    UnlockAchievement(0x02, 0x14, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 6, 0x2316)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['千手钢腕'], 1)"),
            Expr.Return,
        ),
        'loc_650',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['千手钢腕']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x2316)

    Jump('loc_6B6')

    def _loc_650(): pass

    label('loc_650')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['千手钢腕']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['千手钢腕']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0x00000000)

    def _loc_6B6(): pass

    label('loc_6B6')

    Jump('loc_6EA')

    def _loc_6B9(): pass

    label('loc_6B9')

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
    def _loc_6EA(): pass

    label('loc_6EA')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x6F8
@scena.Code('func_06_6F8')
def func_06_6F8():
    UnlockAchievement(0x02, 0x15, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0462, 7, 0x2317)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D5',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000B, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_76C',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x2317)

    Jump('loc_7D2')

    def _loc_76C(): pass

    label('loc_76C')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0x00000000)

    def _loc_7D2(): pass

    label('loc_7D2')

    Jump('loc_806')

    def _loc_7D5(): pass

    label('loc_7D5')

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
    def _loc_806(): pass

    label('loc_806')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
