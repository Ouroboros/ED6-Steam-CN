import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0701_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0701   ._SN')

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
    TXT(0x0B, ''),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0701.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xE40
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
        ('ED6_DT29/CH12590._CH', 'ED6_DT29/CH12590P._CP'),
        ('ED6_DT29/CH12591._CH', 'ED6_DT29/CH12591P._CP'),
        ('ED6_DT29/CH12600._CH', 'ED6_DT29/CH12600P._CP'),
        ('ED6_DT29/CH12601._CH', 'ED6_DT29/CH12601P._CP'),
        ('ED6_DT29/CH12610._CH', 'ED6_DT29/CH12610P._CP'),
        ('ED6_DT29/CH12611._CH', 'ED6_DT29/CH12611P._CP'),
        ('ED6_DT29/CH12620._CH', 'ED6_DT29/CH12620P._CP'),
        ('ED6_DT29/CH12621._CH', 'ED6_DT29/CH12621P._CP'),
        ('ED6_DT29/CH12630._CH', 'ED6_DT29/CH12630P._CP'),
        ('ED6_DT29/CH12631._CH', 'ED6_DT29/CH12631P._CP'),
        ('ED6_DT29/CH12640._CH', 'ED6_DT29/CH12640P._CP'),
        ('ED6_DT29/CH12641._CH', 'ED6_DT29/CH12641P._CP'),
        ('ED6_DT29/CH12652._CH', 'ED6_DT29/CH12652P._CP'),
        ('ED6_DT29/CH12652._CH', 'ED6_DT29/CH12652P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 680,
            z           = 400,
            y           = 47850,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E9,
            word_18     = 0x1FC2,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 0,
            z           = -50,
            y           = 0,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FC3,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 25540,
            z           = 0,
            y           = 47760,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FC4,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 45190,
            z           = 7600,
            y           = 7900,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FC5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -46750,
            z           = 400,
            y           = 4450,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E9,
            word_18     = 0x1FC6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -47010,
            z           = 400,
            y           = -7800,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FC7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 29120,
            z           = 400,
            y           = -29450,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FC8,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 37280,
            z           = 400,
            y           = -37230,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E9,
            word_18     = 0x1FC9,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 330,
            z           = 0,
            y           = -70120,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FCA,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5350,
            z           = 400,
            y           = -76120,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FCB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5780,
            z           = 400,
            y           = -75920,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FCC,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x24E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x24E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 15810,
            triggerZ            = 0,
            triggerY            = -14950,
            triggerRange        = 1000,
            actorX              = 15310,
            actorZ              = 0,
            actorY              = -15440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 32640,
            triggerZ            = 0,
            triggerY            = -33770,
            triggerRange        = 1000,
            actorX              = 33140,
            actorZ              = 0,
            actorY              = -33270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 400,
            triggerY            = -16600,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 400,
            actorY              = -15980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -16300,
            triggerZ            = 7600,
            triggerY            = -50,
            triggerRange        = 1000,
            actorX              = -16980,
            actorZ              = 7600,
            actorY              = -50,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2DE
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2EE'),
        (0x00000065, 'loc_2F5'),
        (-1, 'loc_2FC'),
    )

    def _loc_2EE(): pass

    label('loc_2EE')

    Event(0, 0x0006)

    Jump('loc_2FC')

    def _loc_2F5(): pass

    label('loc_2F5')

    Event(0, 0x0008)

    Jump('loc_2FC')

    def _loc_2FC(): pass

    label('loc_2FC')

    Return()

# id: 0x0001 offset: 0x2FD
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 1, 0x1F01)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30F',
    )

    OP_6F(0x0000, 0)

    Jump('loc_316')

    def _loc_30F(): pass

    label('loc_30F')

    OP_6F(0x0000, 60)

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 2, 0x1F02)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_328',
    )

    OP_6F(0x0001, 0)

    Jump('loc_32F')

    def _loc_328(): pass

    label('loc_328')

    OP_6F(0x0001, 60)

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 3, 0x1F03)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_341',
    )

    OP_6F(0x0002, 0)

    Jump('loc_348')

    def _loc_341(): pass

    label('loc_341')

    OP_6F(0x0002, 60)

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 5, 0x1F05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_6F(0x0003, 0)

    Jump('loc_361')

    def _loc_35A(): pass

    label('loc_35A')

    OP_6F(0x0003, 60)

    def _loc_361(): pass

    label('loc_361')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 2, 0x1FC2)),
            Expr.Return,
        ),
        'loc_395',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_395(): pass

    label('loc_395')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 3, 0x1FC3)),
            Expr.Return,
        ),
        'loc_3A1',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_3A1(): pass

    label('loc_3A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 4, 0x1FC4)),
            Expr.Return,
        ),
        'loc_3AD',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_3AD(): pass

    label('loc_3AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 5, 0x1FC5)),
            Expr.Return,
        ),
        'loc_3B9',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 6, 0x1FC6)),
            Expr.Return,
        ),
        'loc_3C5',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F8, 7, 0x1FC7)),
            Expr.Return,
        ),
        'loc_3D1',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_3D1(): pass

    label('loc_3D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 0, 0x1FC8)),
            Expr.Return,
        ),
        'loc_3DD',
    )

    SetChrFlags(0x000E, 0x0080)

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 1, 0x1FC9)),
            Expr.Return,
        ),
        'loc_3E9',
    )

    SetChrFlags(0x000F, 0x0080)

    def _loc_3E9(): pass

    label('loc_3E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 2, 0x1FCA)),
            Expr.Return,
        ),
        'loc_3F5',
    )

    SetChrFlags(0x0010, 0x0080)

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 3, 0x1FCB)),
            Expr.Return,
        ),
        'loc_401',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F9, 4, 0x1FCC)),
            Expr.Return,
        ),
        'loc_40D',
    )

    SetChrFlags(0x0012, 0x0080)

    def _loc_40D(): pass

    label('loc_40D')

    ExecExpressionWithValue(
        0x0009,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1B(0x00, 0x00, 0x0007)
    OP_1B(0x01, 0x00, 0x0009)

    Return()

# id: 0x0002 offset: 0x444
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x15, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 1, 0x1F01)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_521',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_4B8',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F01)

    Jump('loc_51E')

    def _loc_4B8(): pass

    label('loc_4B8')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
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

    def _loc_51E(): pass

    label('loc_51E')

    Jump('loc_552')

    def _loc_521(): pass

    label('loc_521')

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
    def _loc_552(): pass

    label('loc_552')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x560
@scena.Code('func_03_560')
def func_03_560():
    UnlockAchievement(0x02, 0x16, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 2, 0x1F02)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63D',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_5D4',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F02)

    Jump('loc_63A')

    def _loc_5D4(): pass

    label('loc_5D4')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_63A(): pass

    label('loc_63A')

    Jump('loc_66E')

    def _loc_63D(): pass

    label('loc_63D')

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
    def _loc_66E(): pass

    label('loc_66E')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x67C
@scena.Code('func_04_67C')
def func_04_67C():
    UnlockAchievement(0x02, 0x17, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 3, 0x1F03)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['古剑'], 1)"),
            Expr.Return,
        ),
        'loc_6F0',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['古剑']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F03)

    Jump('loc_756')

    def _loc_6F0(): pass

    label('loc_6F0')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['古剑']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['古剑']),
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

    def _loc_756(): pass

    label('loc_756')

    Jump('loc_78A')

    def _loc_759(): pass

    label('loc_759')

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
    def _loc_78A(): pass

    label('loc_78A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x798
@scena.Code('func_05_798')
def func_05_798():
    UnlockAchievement(0x02, 0x18, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E0, 5, 0x1F05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_875',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['魅惑项圈'], 1)"),
            Expr.Return,
        ),
        'loc_80C',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['魅惑项圈']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F05)

    Jump('loc_872')

    def _loc_80C(): pass

    label('loc_80C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['魅惑项圈']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['魅惑项圈']),
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

    def _loc_872(): pass

    label('loc_872')

    Jump('loc_8A6')

    def _loc_875(): pass

    label('loc_875')

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
    def _loc_8A6(): pass

    label('loc_8A6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8B4
@scena.Code('func_06_8B4')
def func_06_8B4():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 200, 84750, 0)
    SetChrPos(0x0101, 500, -50, 84250, 180)
    SetChrPos(0x0102, -500, -50, 84250, 180)
    SetChrPos(0x00F8, 500, -50, 85250, 180)
    SetChrPos(0x00F9, -500, -50, 85250, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x000A)
    Call(0, 0x000C)
    Fade(500)
    OP_6D(80, 200, 82700, 0)
    SetChrPos(0x0000, 80, 200, 82700, 180)
    SetChrPos(0x0001, 80, 200, 82700, 180)
    SetChrPos(0x0002, 80, 200, 82700, 180)
    SetChrPos(0x0003, 80, 200, 82700, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0007 offset: 0x9B4
@scena.Code('func_07_9B4')
def func_07_9B4():
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
    OP_6D(0, 200, 84750, 0)
    SetChrPos(0x0101, -500, -50, 85250, 0)
    SetChrPos(0x0102, 500, -50, 85250, 0)
    SetChrPos(0x00F8, -500, -50, 84250, 0)
    SetChrPos(0x00F9, 500, -50, 84250, 0)
    OP_0D()
    Call(0, 0x000A)
    Call(0, 0x000D)
    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT21/C0700._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0xA37
@scena.Code('func_08_A37')
def func_08_A37():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 3800, -124480, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, -500, 3800, -123980, 0)
    SetChrPos(0x0102, 500, 3800, -123980, 0)
    SetChrPos(0x00F8, -500, 3800, -124980, 0)
    SetChrPos(0x00F9, 500, 3800, -124980, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000C)
    Fade(500)
    OP_6D(80, 3550, -120330, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, 80, 3550, -120330, 0)
    SetChrPos(0x0001, 80, 3550, -120330, 0)
    SetChrPos(0x0002, 80, 3550, -120330, 0)
    SetChrPos(0x0003, 80, 3550, -120330, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0009 offset: 0xB49
@scena.Code('func_09_B49')
def func_09_B49():
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
    OP_6D(0, 3800, -124480, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 500, 3800, -124980, 180)
    SetChrPos(0x0102, -500, 3800, -124980, 180)
    SetChrPos(0x00F8, 500, 3800, -123980, 180)
    SetChrPos(0x00F9, -500, 3800, -123980, 180)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000D)
    NewScene('ED6_DT21/C0702._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0xBCA
@scena.Code('func_0A_BCA')
def func_0A_BCA():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x000B offset: 0xCA9
@scena.Code('func_0B_CA9')
def func_0B_CA9():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x000C offset: 0xD88
@scena.Code('func_0C_D88')
def func_0C_D88():
    @scena.Lambda('lambda_0D8E')
    def lambda_0D8E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0D8E)

    @scena.Lambda('lambda_0DA0')
    def lambda_0DA0():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0DA0)

    @scena.Lambda('lambda_0DB2')
    def lambda_0DB2():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0DB2)

    @scena.Lambda('lambda_0DC4')
    def lambda_0DC4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0DC4)

    Sleep(2500)

    Return()

# id: 0x000D offset: 0xDD6
@scena.Code('func_0D_DD6')
def func_0D_DD6():
    @scena.Lambda('lambda_0DDC')
    def lambda_0DDC():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0DDC)

    @scena.Lambda('lambda_0DEE')
    def lambda_0DEE():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0DEE)

    @scena.Lambda('lambda_0E00')
    def lambda_0E00():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0E00)

    @scena.Lambda('lambda_0E12')
    def lambda_0E12():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0E12)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
