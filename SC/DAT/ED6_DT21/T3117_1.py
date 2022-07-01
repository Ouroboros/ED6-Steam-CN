import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3117_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3117_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3117_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x604
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
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x382),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5',
    )

    Return()

    def _loc_B5(): pass

    label('loc_B5')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0xE4E5A8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_149',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x14E6),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1298),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_149',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_149(): pass

    label('loc_149')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0080)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C8',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x157C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x150E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1C8',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1C8(): pass

    label('loc_1C8')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0100)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_247',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1176),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x37D2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_247',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_247(): pass

    label('loc_247')

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0200)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C6',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x6D6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x31D8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2C6',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2C6(): pass

    label('loc_2C6')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    LoadEffect(0x00, 'map\\\\mp108_00.eff')
    PlayEffect(0x00, 0x00, 0x0000, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0xF4240),
            Expr.Leq,
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D1',
    )

    EventBegin(0x01)
    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0000)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x7),
            Expr.Return,
        ),
        (0x00000001, 'loc_3B0'),
        (0x00000002, 'loc_3B7'),
        (0x00000003, 'loc_3BE'),
        (0x00000004, 'loc_3C5'),
        (-1, 'loc_3CC'),
    )

    def _loc_3B0(): pass

    label('loc_3B0')

    OP_65(0x00, 0x0001)

    Jump('loc_3CC')

    def _loc_3B7(): pass

    label('loc_3B7')

    OP_65(0x01, 0x0001)

    Jump('loc_3CC')

    def _loc_3BE(): pass

    label('loc_3BE')

    OP_65(0x02, 0x0001)

    Jump('loc_3CC')

    def _loc_3C5(): pass

    label('loc_3C5')

    OP_65(0x03, 0x0001)

    Jump('loc_3CC')

    def _loc_3CC(): pass

    label('loc_3CC')

    EventEnd(0x01)

    Jump('loc_4A7')

    def _loc_3D1(): pass

    label('loc_3D1')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x4C4B40),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_421',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这附近有反应！',
            TxtCtl.Enter,
        ),
    )

    OP_22(0x00AA, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_4A7')

    def _loc_421(): pass

    label('loc_421')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x989680),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_46D',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近有反应',
            TxtCtl.Enter,
        ),
    )

    OP_22(0x00AA, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_4A7')

    def _loc_46D(): pass

    label('loc_46D')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没有反应',
            TxtCtl.Enter,
        ),
    )

    OP_22(0x00AB, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_4A7(): pass

    label('loc_4A7')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0001 offset: 0x4AE
@scena.Code('Init')
def Init():
    EventBegin(0x01)
    OP_22(0x0011, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0040)
    OP_64(0x00, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x0002 offset: 0x501
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x01)
    OP_22(0x0011, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0080)
    OP_64(0x01, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x0003 offset: 0x554
@scena.Code('func_03_554')
def func_03_554():
    EventBegin(0x01)
    OP_22(0x0011, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0100)
    OP_64(0x02, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x0004 offset: 0x5A7
@scena.Code('func_04_5A7')
def func_04_5A7():
    EventBegin(0x01)
    OP_22(0x0011, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0200)
    OP_64(0x03, 0x0001)
    EventEnd(0x01)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
