import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2115_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2115   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2115.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA6C
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
        ('ED6_DT09/CH10560._CH', 'ED6_DT09/CH10560P._CP'),
        ('ED6_DT09/CH10561._CH', 'ED6_DT09/CH10561P._CP'),
        ('ED6_DT09/CH10570._CH', 'ED6_DT09/CH10570P._CP'),
        ('ED6_DT09/CH10571._CH', 'ED6_DT09/CH10571P._CP'),
        ('ED6_DT09/CH10580._CH', 'ED6_DT09/CH10580P._CP'),
        ('ED6_DT09/CH10581._CH', 'ED6_DT09/CH10581P._CP'),
        ('ED6_DT09/CH10590._CH', 'ED6_DT09/CH10590P._CP'),
        ('ED6_DT09/CH10591._CH', 'ED6_DT09/CH10591P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 3970,
            z           = 0,
            y           = 3770,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01B9,
            word_18     = 0x1359,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x106
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x106
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -8230,
            triggerZ            = 0,
            triggerY            = 8330,
            triggerRange        = 1000,
            actorX              = -8730,
            actorZ              = 0,
            actorY              = 8830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9350,
            triggerZ            = 0,
            triggerY            = 9330,
            triggerRange        = 1000,
            actorX              = 8850,
            actorZ              = 0,
            actorY              = 8830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12530,
            triggerZ            = 0,
            triggerY            = -660,
            triggerRange        = 1000,
            actorX              = 12530,
            actorZ              = 0,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12430,
            triggerZ            = 0,
            triggerY            = -640,
            triggerRange        = 1000,
            actorX              = -12400,
            actorZ              = 0,
            actorY              = 150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4470,
            triggerZ            = 0,
            triggerY            = 22500,
            triggerRange        = 1000,
            actorX              = 4690,
            actorZ              = 0,
            actorY              = 23200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3680,
            triggerZ            = 380,
            triggerY            = 490,
            triggerRange        = 1000,
            actorX              = 10,
            actorZ              = 380,
            actorY              = 180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1DF
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 6, 0x1316)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F1',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1F8')

    def _loc_1F1(): pass

    label('loc_1F1')

    OP_6F(0x0000, 60)

    def _loc_1F8(): pass

    label('loc_1F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 0, 0x1318)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20A',
    )

    OP_6F(0x0001, 0)

    Jump('loc_211')

    def _loc_20A(): pass

    label('loc_20A')

    OP_6F(0x0001, 60)

    def _loc_211(): pass

    label('loc_211')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 2, 0x131A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_223',
    )

    OP_6F(0x0002, 0)

    Jump('loc_22A')

    def _loc_223(): pass

    label('loc_223')

    OP_6F(0x0002, 60)

    def _loc_22A(): pass

    label('loc_22A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 4, 0x131C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23C',
    )

    OP_6F(0x0003, 0)

    Jump('loc_243')

    def _loc_23C(): pass

    label('loc_23C')

    OP_6F(0x0003, 60)

    def _loc_243(): pass

    label('loc_243')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 7, 0x131F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_255',
    )

    OP_6F(0x0004, 0)

    Jump('loc_25C')

    def _loc_255(): pass

    label('loc_255')

    OP_6F(0x0004, 60)

    def _loc_25C(): pass

    label('loc_25C')

    OP_E0(0x02, 0xA2, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x6A, 0x04, 0x00, 0x00)
    OP_E0(0x03, 0x5E, 0xCF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x6A, 0x04, 0x00, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026B, 1, 0x1359)),
            Expr.Return,
        ),
        'loc_284',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_284(): pass

    label('loc_284')

    OP_25(0x01CB, 0xFFFFFFA6, 0x00000000, 0x00000096, 0x000007D0, 0x000061A8, 0x64, 0x00000000)

    Return()

# id: 0x0002 offset: 0x2A1
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x89, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 6, 0x1316)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['木底鞋'], 1)"),
            Expr.Return,
        ),
        'loc_315',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['木底鞋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1316)

    Jump('loc_37B')

    def _loc_315(): pass

    label('loc_315')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['木底鞋']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['木底鞋']),
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

    def _loc_37B(): pass

    label('loc_37B')

    Jump('loc_3AF')

    def _loc_37E(): pass

    label('loc_37E')

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
    def _loc_3AF(): pass

    label('loc_3AF')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x3BD
@scena.Code('func_03_3BD')
def func_03_3BD():
    UnlockAchievement(0x02, 0x8A, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 0, 0x1318)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['杰尼丝水手服'], 1)"),
            Expr.Return,
        ),
        'loc_431',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['杰尼丝水手服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1318)

    Jump('loc_497')

    def _loc_431(): pass

    label('loc_431')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['杰尼丝水手服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['杰尼丝水手服']),
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

    def _loc_497(): pass

    label('loc_497')

    Jump('loc_4CB')

    def _loc_49A(): pass

    label('loc_49A')

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
    def _loc_4CB(): pass

    label('loc_4CB')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4D9
@scena.Code('func_04_4D9')
def func_04_4D9():
    UnlockAchievement(0x02, 0x8B, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 2, 0x131A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B6',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['珍珠耳环'], 1)"),
            Expr.Return,
        ),
        'loc_54D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['珍珠耳环']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x131A)

    Jump('loc_5B3')

    def _loc_54D(): pass

    label('loc_54D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['珍珠耳环']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['珍珠耳环']),
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

    def _loc_5B3(): pass

    label('loc_5B3')

    Jump('loc_5E7')

    def _loc_5B6(): pass

    label('loc_5B6')

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
    def _loc_5E7(): pass

    label('loc_5E7')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5F5
@scena.Code('func_05_5F5')
def func_05_5F5():
    UnlockAchievement(0x02, 0x8C, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 4, 0x131C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D2',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['黑檀之杖'], 1)"),
            Expr.Return,
        ),
        'loc_669',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['黑檀之杖']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x131C)

    Jump('loc_6CF')

    def _loc_669(): pass

    label('loc_669')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['黑檀之杖']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['黑檀之杖']),
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

    def _loc_6CF(): pass

    label('loc_6CF')

    Jump('loc_703')

    def _loc_6D2(): pass

    label('loc_6D2')

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
    def _loc_703(): pass

    label('loc_703')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x711
@scena.Code('func_06_711')
def func_06_711():
    UnlockAchievement(0x02, 0x8D, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0263, 7, 0x131F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7EE',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['危险肉丸'], 1)"),
            Expr.Return,
        ),
        'loc_785',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x131F)

    Jump('loc_7EB')

    def _loc_785(): pass

    label('loc_785')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['危险肉丸']),
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

    def _loc_7EB(): pass

    label('loc_7EB')

    Jump('loc_81F')

    def _loc_7EE(): pass

    label('loc_7EE')

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
    def _loc_81F(): pass

    label('loc_81F')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_877',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0028)"),
            Expr.Return,
        ),
        'loc_83E',
    )

    Jump('loc_877')

    def _loc_83E(): pass

    label('loc_83E')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_877(): pass

    label('loc_877')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x880
@scena.Code('func_07_880')
def func_07_880():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08B8')
    def lambda_08B8():
        OP_6D(-1110, 380, 470, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_08B8)

    @scena.Lambda('lambda_08D0')
    def lambda_08D0():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_08D0)

    @scena.Lambda('lambda_08E8')
    def lambda_08E8():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_08E8)

    @scena.Lambda('lambda_08F8')
    def lambda_08F8():
        OP_6C(225000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_08F8)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
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
            TXT(0x00, '钓鱼\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A4C',
    )

    OP_C0(0x0E, 0x0000001D, 0xFFFFF40C, 0x00000370, 0x000001D6, 0x0000005A, 0xFFFFFC36, 0xFFFFFE0C, 0x00000262)
    Fade(500)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)
    ClearChrFlags(0x0004, 0x0008)
    ClearChrFlags(0x0005, 0x0008)
    ClearChrFlags(0x0006, 0x0008)
    ClearChrFlags(0x0007, 0x0008)
    SetChrChipByIndex(0x0000, 65535)
    ClearChrFlags(0x0000, 0x0002)
    ClearChrFlags(0x0000, 0x0040)
    ClearChrFlags(0x0000, 0x0004)
    SetChrPos(0x0000, -3760, 380, 160, 90)
    SetChrPos(0x0001, -3760, 380, 160, 90)
    SetChrPos(0x0002, -3760, 380, 160, 90)
    SetChrPos(0x0003, -3760, 380, 160, 90)
    SetChrPos(0x0004, -3760, 380, 160, 90)
    SetChrPos(0x0005, -3760, 380, 160, 90)
    SetChrPos(0x0006, -3760, 380, 160, 90)
    SetChrPos(0x0007, -3760, 380, 160, 90)
    OP_69(0x0000, 0x00000000)
    OP_30(0x00)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_A5B')

    def _loc_A4C(): pass

    label('loc_A4C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A5B',
    )

    EventEnd(0x01)

    def _loc_A5B(): pass

    label('loc_A5B')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
