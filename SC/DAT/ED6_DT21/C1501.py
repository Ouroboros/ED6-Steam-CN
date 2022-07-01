import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1501_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1501   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '帝王巨蝎'),
    TXT(0x02, '玛诺利亚海岸方向'),
    TXT(0x03, '古罗尼山道·关所方向'),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1501.x'
    header.mapIndex       = 61
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x698
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
        ('ED6_DT29/CH12550._CH', 'ED6_DT29/CH12550P._CP'),
        ('ED6_DT29/CH12551._CH', 'ED6_DT29/CH12551P._CP'),
        ('ED6_DT29/CH12440._CH', 'ED6_DT29/CH12440P._CP'),
        ('ED6_DT29/CH12441._CH', 'ED6_DT29/CH12441P._CP'),
    ]

# id: 0x10002 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -96470,
            z                   = 3990,
            y                   = 82150,
            direction           = 188,
            word_0E             = 2,
            dword_10            = 131072,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -68830,
            z                   = 70,
            y                   = -31470,
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
            x                   = -114600,
            z                   = 6050,
            y                   = 118780,
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

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -106080,
            z           = 6030,
            y           = 93200,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00C9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -104200,
            z           = 1980,
            y           = 7590,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00C9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -109430,
            z           = 4040,
            y           = 46760,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00C9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -121470,
            z           = 2040,
            y           = 22550,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00C9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -91580,
            y           = 3000,
            z           = 77390,
            range       = -102500,
            dword_10    = 0x0000173E,
            dword_14    = 0x00013D76,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -106310,
            triggerZ            = 1990,
            triggerY            = 2710,
            triggerRange        = 1000,
            actorX              = -106430,
            actorZ              = 1990,
            actorY              = 2090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -112480,
            triggerZ            = 2070,
            triggerY            = 63130,
            triggerRange        = 1000,
            actorX              = -112990,
            actorZ              = 2070,
            actorY              = 63430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x202
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x203
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFC8560, 0xFFFEA840, 0x0023003F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_233',
    )

    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_245')

    def _loc_233(): pass

    label('loc_233')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 3, 0x12FB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_245',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_245(): pass

    label('loc_245')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 5, 0x130D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_257',
    )

    OP_6F(0x0000, 0)

    Jump('loc_25E')

    def _loc_257(): pass

    label('loc_257')

    OP_6F(0x0000, 60)

    def _loc_25E(): pass

    label('loc_25E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 6, 0x130E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_270',
    )

    OP_6F(0x0001, 0)

    Jump('loc_277')

    def _loc_270(): pass

    label('loc_270')

    OP_6F(0x0001, 60)

    def _loc_277(): pass

    label('loc_277')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x283
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_298',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_298(): pass

    label('loc_298')

    Return()

# id: 0x0003 offset: 0x299
@scena.Code('func_03_299')
def func_03_299():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 3, 0x12FB)),
            Expr.Return,
        ),
        'loc_2A1',
    )

    Return()

    def _loc_2A1(): pass

    label('loc_2A1')

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

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

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
        (0x00000001, 'loc_386'),
        (-1, 'loc_3A9'),
    )

    def _loc_386(): pass

    label('loc_386')

    Fade(500)
    OP_89(0x0000, -97890, 3940, 74670, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_3A9(): pass

    label('loc_3A9')

    Battle(0x00000EDE, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -97890, 3940, 74670, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_3E2'),
        (0x00000001, 'loc_3E5'),
        (-1, 'loc_3E8'),
    )

    def _loc_3E2(): pass

    label('loc_3E2')

    EventEnd(0x00)

    Return()

    def _loc_3E5(): pass

    label('loc_3E5')

    OP_B4(0x00)

    Return()

    def _loc_3E8(): pass

    label('loc_3E8')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x12FB)
    OP_28(0x00A2, 0x04, 0x10)
    OP_28(0x00A2, 0x04, 0x02)
    OP_28(0x00A2, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x454
@scena.Code('func_04_454')
def func_04_454():
    UnlockAchievement(0x02, 0x5A, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 5, 0x130D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_531',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_4C8',
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
    OP_A2(0x130D)

    Jump('loc_52E')

    def _loc_4C8(): pass

    label('loc_4C8')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_52E(): pass

    label('loc_52E')

    Jump('loc_562')

    def _loc_531(): pass

    label('loc_531')

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
    def _loc_562(): pass

    label('loc_562')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x570
@scena.Code('func_05_570')
def func_05_570():
    UnlockAchievement(0x02, 0x5B, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0261, 6, 0x130E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64D',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['酒肴『薄红仕立』'], 1)"),
            Expr.Return,
        ),
        'loc_5E4',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['酒肴『薄红仕立』']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x130E)

    Jump('loc_64A')

    def _loc_5E4(): pass

    label('loc_5E4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['酒肴『薄红仕立』']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['酒肴『薄红仕立』']),
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

    def _loc_64A(): pass

    label('loc_64A')

    Jump('loc_67E')

    def _loc_64D(): pass

    label('loc_64D')

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
    def _loc_67E(): pass

    label('loc_67E')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
