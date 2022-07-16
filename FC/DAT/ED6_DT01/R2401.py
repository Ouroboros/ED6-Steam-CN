import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '盔甲巨蟹'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2401.x'
    header.mapIndex       = 103
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5BB
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
            word_3A         = 103,
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
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -10540,
            z                   = 400,
            y                   = 71630,
            direction           = 134,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0xDA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xDA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -10540,
            y           = -1000,
            z           = 71630,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 10960,
            triggerZ            = -50,
            triggerY            = 86080,
            triggerRange        = 1000,
            actorX              = 11490,
            actorZ              = 1000,
            actorY              = 86480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x11E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x11F
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -130000, -79000, 196644)
    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            (Expr.Eval, "OP_29(0x0026, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0026, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0094, 2, 0x4A2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15F',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_15F(): pass

    label('loc_15F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 0, 0x4C8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_171',
    )

    OP_6F(0x0000, 0)

    Jump('loc_178')

    def _loc_171(): pass

    label('loc_171')

    OP_6F(0x0000, 60)

    def _loc_178(): pass

    label('loc_178')

    Return()

# id: 0x0002 offset: 0x179
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_18E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_18E(): pass

    label('loc_18E')

    Return()

# id: 0x0003 offset: 0x18F
@scena.Code('func_03_18F')
def func_03_18F():
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
        (0x00000001, 'loc_274'),
        (-1, 'loc_30E'),
    )

    def _loc_274(): pass

    label('loc_274')

    Fade(1000)
    SetChrPos(0x0000, -5890, -30, 69910, 276)
    SetChrPos(0x0001, -5890, -30, 69910, 276)
    SetChrPos(0x0002, -5890, -30, 69910, 276)
    SetChrPos(0x0003, -5890, -30, 69910, 276)
    SetChrPos(0x0004, -5890, -30, 69910, 276)
    SetChrPos(0x0005, -5890, -30, 69910, 276)
    SetChrPos(0x0006, -5890, -30, 69910, 276)
    SetChrPos(0x0007, -5890, -30, 69910, 276)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_30E(): pass

    label('loc_30E')

    Battle(0x000003FD, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrPos(0x0000, -5890, -30, 69910, 276)
    SetChrPos(0x0001, -5890, -30, 69910, 276)
    SetChrPos(0x0002, -5890, -30, 69910, 276)
    SetChrPos(0x0003, -5890, -30, 69910, 276)
    SetChrPos(0x0004, -5890, -30, 69910, 276)
    SetChrPos(0x0005, -5890, -30, 69910, 276)
    SetChrPos(0x0006, -5890, -30, 69910, 276)
    SetChrPos(0x0007, -5890, -30, 69910, 276)
    OP_69(0x0000, 0)
    OP_30(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_3BC'),
        (0x00000001, 'loc_3BF'),
        (-1, 'loc_3C2'),
    )

    def _loc_3BC(): pass

    label('loc_3BC')

    EventEnd(0x00)

    Return()

    def _loc_3BF(): pass

    label('loc_3BF')

    OP_B4(0x00)

    Return()

    def _loc_3C2(): pass

    label('loc_3C2')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '成功消灭了阿伊纳街道中被通缉的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0026, 0x04, 0x10)
    OP_28(0x0026, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x0094, 2, 0x4A2))
    Sleep(400)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '试·零式导力枪',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x0067, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x483
@scena.Code('func_04_483')
def func_04_483():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0099, 0, 0x4C8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_4F7',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0099, 0, 0x4C8))

    Jump('loc_56A')

    def _loc_4F7(): pass

    label('loc_4F7')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_56A(): pass

    label('loc_56A')

    Jump('loc_5A3')

    def _loc_56D(): pass

    label('loc_56D')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x8B)
    def _loc_5A3(): pass

    label('loc_5A3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
