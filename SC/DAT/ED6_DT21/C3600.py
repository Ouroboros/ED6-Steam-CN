import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3600   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3600.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x14D3
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 30,
            triggerZ            = -7650,
            triggerY            = -710,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = -7650,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4990,
            triggerZ            = -7200,
            triggerY            = -5010,
            triggerRange        = 1000,
            actorX              = -5460,
            actorZ              = -7200,
            actorY              = -5470,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -7190,
            triggerZ            = -7200,
            triggerY            = 10,
            triggerRange        = 1000,
            actorX              = -7810,
            actorZ              = -7200,
            actorY              = 10,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4970,
            triggerZ            = -7200,
            triggerY            = 5030,
            triggerRange        = 1000,
            actorX              = -5440,
            actorZ              = -7200,
            actorY              = 5500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5020,
            triggerZ            = -7200,
            triggerY            = 4990,
            triggerRange        = 1000,
            actorX              = 5450,
            actorZ              = -7200,
            actorY              = 5430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7200,
            triggerZ            = -7200,
            triggerY            = 10,
            triggerRange        = 1000,
            actorX              = 7860,
            actorZ              = -7200,
            actorY              = 10,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4990,
            triggerZ            = -7200,
            triggerY            = -5020,
            triggerRange        = 1000,
            actorX              = 5520,
            actorZ              = -7200,
            actorY              = -5550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A4
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1B4'),
        (0x00000065, 'loc_1BB'),
        (-1, 'loc_1C2'),
    )

    def _loc_1B4(): pass

    label('loc_1B4')

    Event(0, 0x0009)

    Jump('loc_1C2')

    def _loc_1BB(): pass

    label('loc_1BB')

    Event(0, 0x0013)

    Jump('loc_1C2')

    def _loc_1C2(): pass

    label('loc_1C2')

    Return()

# id: 0x0001 offset: 0x1C3
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 0, 0x1F20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D5',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1DC')

    def _loc_1D5(): pass

    label('loc_1D5')

    OP_6F(0x0001, 60)

    def _loc_1DC(): pass

    label('loc_1DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 2, 0x1F22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EE',
    )

    OP_6F(0x0002, 0)

    Jump('loc_1F5')

    def _loc_1EE(): pass

    label('loc_1EE')

    OP_6F(0x0002, 60)

    def _loc_1F5(): pass

    label('loc_1F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 3, 0x1F23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_207',
    )

    OP_6F(0x0003, 0)

    Jump('loc_20E')

    def _loc_207(): pass

    label('loc_207')

    OP_6F(0x0003, 60)

    def _loc_20E(): pass

    label('loc_20E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 4, 0x1F24)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_220',
    )

    OP_6F(0x0004, 0)

    Jump('loc_227')

    def _loc_220(): pass

    label('loc_220')

    OP_6F(0x0004, 60)

    def _loc_227(): pass

    label('loc_227')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 5, 0x1F25)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_239',
    )

    OP_6F(0x0005, 0)

    Jump('loc_240')

    def _loc_239(): pass

    label('loc_239')

    OP_6F(0x0005, 60)

    def _loc_240(): pass

    label('loc_240')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 6, 0x1F26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_252',
    )

    OP_6F(0x0006, 0)

    Jump('loc_259')

    def _loc_252(): pass

    label('loc_252')

    OP_6F(0x0006, 60)

    def _loc_259(): pass

    label('loc_259')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 6, 0x1F26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26B',
    )

    OP_6F(0x0007, 0)

    Jump('loc_272')

    def _loc_26B(): pass

    label('loc_26B')

    OP_6F(0x0007, 60)

    def _loc_272(): pass

    label('loc_272')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')
    OP_1B(0x00, 0x00, 0x000E)
    OP_1B(0x01, 0x00, 0x0014)

    Return()

# id: 0x0002 offset: 0x2A5
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xD5, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 0, 0x1F20)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000001E)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x02, 0x012C)
    AddSepith(0x04, 0x0064)
    AddSepith(0x05, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×３００\n',
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
    OP_A2(0x1F20)

    Jump('loc_394')

    def _loc_37A(): pass

    label('loc_37A')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_394(): pass

    label('loc_394')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x3A6
@scena.Code('func_03_3A6')
def func_03_3A6():
    UnlockAchievement(0x02, 0xD6, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 2, 0x1F22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_483',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_41A',
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
    OP_A2(0x1F22)

    Jump('loc_480')

    def _loc_41A(): pass

    label('loc_41A')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_480(): pass

    label('loc_480')

    Jump('loc_4B4')

    def _loc_483(): pass

    label('loc_483')

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
    def _loc_4B4(): pass

    label('loc_4B4')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x4C2
@scena.Code('func_04_4C2')
def func_04_4C2():
    UnlockAchievement(0x02, 0xD7, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 3, 0x1F23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_59F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_536',
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
    OP_A2(0x1F23)

    Jump('loc_59C')

    def _loc_536(): pass

    label('loc_536')

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
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_59C(): pass

    label('loc_59C')

    Jump('loc_5D0')

    def _loc_59F(): pass

    label('loc_59F')

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
    def _loc_5D0(): pass

    label('loc_5D0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x5DE
@scena.Code('func_05_5DE')
def func_05_5DE():
    UnlockAchievement(0x02, 0xD8, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 4, 0x1F24)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BB',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_652',
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
    OP_A2(0x1F24)

    Jump('loc_6B8')

    def _loc_652(): pass

    label('loc_652')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_6B8(): pass

    label('loc_6B8')

    Jump('loc_6EC')

    def _loc_6BB(): pass

    label('loc_6BB')

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
    def _loc_6EC(): pass

    label('loc_6EC')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x6FA
@scena.Code('func_06_6FA')
def func_06_6FA():
    UnlockAchievement(0x02, 0xD9, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 5, 0x1F25)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7D7',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['棕榈之药'], 1)"),
            Expr.Return,
        ),
        'loc_76E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F25)

    Jump('loc_7D4')

    def _loc_76E(): pass

    label('loc_76E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['棕榈之药']),
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

    def _loc_7D4(): pass

    label('loc_7D4')

    Jump('loc_808')

    def _loc_7D7(): pass

    label('loc_7D7')

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
    def _loc_808(): pass

    label('loc_808')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x816
@scena.Code('func_07_816')
def func_07_816():
    UnlockAchievement(0x02, 0xDA, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 6, 0x1F26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F3',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_88A',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F26)

    Jump('loc_8F0')

    def _loc_88A(): pass

    label('loc_88A')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0x00000000)

    def _loc_8F0(): pass

    label('loc_8F0')

    Jump('loc_924')

    def _loc_8F3(): pass

    label('loc_8F3')

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
    def _loc_924(): pass

    label('loc_924')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x932
@scena.Code('func_08_932')
def func_08_932():
    UnlockAchievement(0x02, 0xDB, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E4, 7, 0x1F27)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A0F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0007, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_9A6',
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
    OP_A2(0x1F27)

    Jump('loc_A0C')

    def _loc_9A6(): pass

    label('loc_9A6')

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
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0x00000000)

    def _loc_A0C(): pass

    label('loc_A0C')

    Jump('loc_A40')

    def _loc_A0F(): pass

    label('loc_A0F')

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
    def _loc_A40(): pass

    label('loc_A40')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xA4E
@scena.Code('func_09_A4E')
def func_09_A4E():
    EventBegin(0x00)
    OP_6D(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 0, 1050, -83970, 0)
    SetChrPos(0x0102, 0, 1050, -83970, 0)
    SetChrPos(0x00F8, 0, 1050, -83970, 0)
    SetChrPos(0x00F9, 0, 1050, -83970, 0)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0102, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x00F8, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x00F9, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    ClearChrFlags(0x0101, 0x0001)
    ClearChrFlags(0x0102, 0x0001)
    ClearChrFlags(0x00F8, 0x0001)
    ClearChrFlags(0x00F9, 0x0001)
    OP_C8(0x0200, 0x0046, 'C_PLAC22._CH', 0x00, 0x01F4)
    ShowPlaceName('红莲之塔')
    FadeIn(1000, 0)
    CreateThread(0x0101, 0x00, 0x00, 0x000A)
    Sleep(800)

    @scena.Lambda('lambda_0B5F')
    def lambda_0B5F():
        OP_6D(140, 600, -78810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B5F)

    CreateThread(0x0102, 0x00, 0x00, 0x000B)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, 0x000C)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, 0x000D)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    OP_6D(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 610, 600, -77870, 0)
    SetChrPos(0x0001, 610, 600, -77870, 0)
    SetChrPos(0x0002, 610, 600, -77870, 0)
    SetChrPos(0x0003, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0xC2E
@scena.Code('func_0A_C2E')
def func_0A_C2E():
    @scena.Lambda('lambda_0C34')
    def lambda_0C34():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0C34)

    @scena.Lambda('lambda_0C4E')
    def lambda_0C4E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0C4E)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    OP_22(0x0099, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ClearChrFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0C79')
    def lambda_0C79():
        OP_8F(0x00FE, 610, 600, -77870, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0C79)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000B offset: 0xC99
@scena.Code('func_0B_C99')
def func_0B_C99():
    @scena.Lambda('lambda_0C9F')
    def lambda_0C9F():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0C9F)

    @scena.Lambda('lambda_0CB9')
    def lambda_0CB9():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0CB9)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    OP_22(0x0099, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ClearChrFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0CE4')
    def lambda_0CE4():
        OP_8F(0x00FE, -470, 600, -78090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0CE4)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000C offset: 0xD04
@scena.Code('func_0C_D04')
def func_0C_D04():
    @scena.Lambda('lambda_0D0A')
    def lambda_0D0A():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0D0A)

    @scena.Lambda('lambda_0D24')
    def lambda_0D24():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0D24)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    OP_22(0x0099, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ClearChrFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0D4F')
    def lambda_0D4F():
        OP_8F(0x00FE, 630, 750, -79310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0D4F)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000D offset: 0xD6F
@scena.Code('func_0D_D6F')
def func_0D_D6F():
    @scena.Lambda('lambda_0D75')
    def lambda_0D75():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0D75)

    @scena.Lambda('lambda_0D8F')
    def lambda_0D8F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0D8F)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    OP_22(0x0099, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0001)
    ClearChrFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_0DBA')
    def lambda_0DBA():
        OP_8F(0x00FE, -540, 750, -79320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0DBA)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000E offset: 0xDDA
@scena.Code('func_0E_DDA')
def func_0E_DDA():
    EventBegin(0x00)
    Fade(500)
    ClearMapFlags(0x00000001)
    OP_6D(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 680, 700, -81310, 180)
    SetChrPos(0x0102, -330, 700, -81100, 180)
    SetChrPos(0x00F8, 910, 750, -79600, 180)
    SetChrPos(0x00F9, -270, 750, -79450, 180)
    CreateThread(0x0101, 0x00, 0x00, 0x000F)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, 0x0010)
    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x00, 0x0011)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, 0x0012)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x02000000)
    NewScene('ED6_DT21/R3104._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0xEC0
@scena.Code('func_0F_EC0')
def func_0F_EC0():
    OP_91(0x00FE, 0, 0, -2000, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0F05')
    def lambda_0F05():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F05)

    @scena.Lambda('lambda_0F1F')
    def lambda_0F1F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0F1F)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0010 offset: 0xF45
@scena.Code('func_10_F45')
def func_10_F45():
    OP_91(0x00FE, 0, 0, -2000, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_0F8A')
    def lambda_0F8A():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0F8A)

    @scena.Lambda('lambda_0FA4')
    def lambda_0FA4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_0FA4)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0011 offset: 0xFCA
@scena.Code('func_11_FCA')
def func_11_FCA():
    OP_91(0x00FE, 0, 0, -3000, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_100F')
    def lambda_100F():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_100F)

    @scena.Lambda('lambda_1029')
    def lambda_1029():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1029)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0012 offset: 0x104F
@scena.Code('func_12_104F')
def func_12_104F():
    OP_91(0x00FE, 0, 0, -3000, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_1094')
    def lambda_1094():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1094)

    @scena.Lambda('lambda_10AE')
    def lambda_10AE():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_10AE)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0013 offset: 0x10D4
@scena.Code('func_13_10D4')
def func_13_10D4():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 250, 84530, 0)
    SetChrPos(0x0101, 500, 250, 84030, 180)
    SetChrPos(0x0102, -500, 250, 84030, 180)
    SetChrPos(0x00F8, 500, 250, 85030, 180)
    SetChrPos(0x00F9, -500, 250, 85030, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0017)
    Fade(500)
    OP_6D(-130, 250, 82150, 0)
    SetChrPos(0x0000, -130, 250, 82150, 180)
    SetChrPos(0x0001, -130, 250, 82150, 180)
    SetChrPos(0x0002, -130, 250, 82150, 180)
    SetChrPos(0x0003, -130, 250, 82150, 180)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x11CF
@scena.Code('func_14_11CF')
def func_14_11CF():
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
    OP_6D(0, 250, 84530, 0)
    SetChrPos(0x0101, -500, 250, 85030, 0)
    SetChrPos(0x0102, 500, 250, 85030, 0)
    SetChrPos(0x00F8, -500, 250, 84030, 0)
    SetChrPos(0x00F9, 500, 250, 84030, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0018)
    NewScene('ED6_DT21/C3601._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x1247
@scena.Code('func_15_1247')
def func_15_1247():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0016 offset: 0x1326
@scena.Code('func_16_1326')
def func_16_1326():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0017 offset: 0x1405
@scena.Code('func_17_1405')
def func_17_1405():
    @scena.Lambda('lambda_140B')
    def lambda_140B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_140B)

    @scena.Lambda('lambda_141D')
    def lambda_141D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_141D)

    @scena.Lambda('lambda_142F')
    def lambda_142F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_142F)

    @scena.Lambda('lambda_1441')
    def lambda_1441():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1441)

    Sleep(2500)

    Return()

# id: 0x0018 offset: 0x1453
@scena.Code('func_18_1453')
def func_18_1453():
    @scena.Lambda('lambda_1459')
    def lambda_1459():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1459)

    @scena.Lambda('lambda_146B')
    def lambda_146B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_146B)

    @scena.Lambda('lambda_147D')
    def lambda_147D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_147D)

    @scena.Lambda('lambda_148F')
    def lambda_148F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_148F)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
