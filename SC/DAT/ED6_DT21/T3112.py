import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3112_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3112   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3112.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Event(0, func_02_C4)

    Return()

# id: 0x0001 offset: 0xAD
@scena.Code('func_01_AD')
def func_01_AD():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C3',
    )

    OP_71(0x0000, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_7B()

    def _loc_C3(): pass

    label('loc_C3')

    Return()

# id: 0x0002 offset: 0xC4
@scena.Code('func_02_C4')
def func_02_C4():
    MapClearFlags(0x00000001)
    EventBegin(0x01)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    CameraMove(1400, 0, 4500, 0)
    ChrSetPos(0x0000, 1750, 0, 1370, 90)
    ChrSetPos(0x0001, 1280, 0, 2600, 180)

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13E',
    )

    ChrSetPos(0x0002, 70, 0, 1470, 180)

    def _loc_13E(): pass

    label('loc_13E')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15B',
    )

    ChrSetPos(0x0003, -50, 0, 2600, 180)

    def _loc_15B(): pass

    label('loc_15B')

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_178',
    )

    ChrSetPos(0x0004, -1380, 0, 1470, 180)

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.PushValueByIndex, 0xF),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_195',
    )

    ChrSetPos(0x0005, -1380, 0, 2600, 180)

    def _loc_195(): pass

    label('loc_195')

    Sleep(200)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_237',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '★【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_570')

    def _loc_237(): pass

    label('loc_237')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C1',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '★【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_570')

    def _loc_2C1(): pass

    label('loc_2C1')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34B',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '★【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_570')

    def _loc_34B(): pass

    label('loc_34B')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D5',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '★【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_570')

    def _loc_3D5(): pass

    label('loc_3D5')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45F',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '★【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_570')

    def _loc_45F(): pass

    label('loc_45F')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E9',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '　【 顶楼 】\n'),
            TXT(0x01, '★【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_570')

    def _loc_4E9(): pass

    label('loc_4E9')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_570',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '★【 顶楼 】\n'),
            TXT(0x01, '　【 ５层 】\n'),
            TXT(0x02, '　【 ４层 】\n'),
            TXT(0x03, '　【 ３层 】\n'),
            TXT(0x04, '　【 ２层 】\n'),
            TXT(0x05, '　【 １层 】\n'),
            TXT(0x06, '　【 Ｂ１ 】\n'),
            TXT(0x07, '　【 离开 】\n'),
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_570(): pass

    label('loc_570')

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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A6',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x6),
            (Expr.PushReg, 0x0),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5A6(): pass

    label('loc_5A6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B6',
    )

    Jump('loc_621')

    def _loc_5B6(): pass

    label('loc_5B6')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushReg, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5ED',
    )

    FadeOut(2000, 0, -1)
    PlaySE(103, 0x00, 0x64)
    CameraMove(1400, -11900, 4500, 2000)
    OP_0D()
    Sleep(800)

    OP_23(0x0067)

    Jump('loc_621')

    def _loc_5ED(): pass

    label('loc_5ED')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushReg, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_621',
    )

    FadeOut(2000, 0, -1)
    PlaySE(103, 0x00, 0x64)
    CameraMove(1400, 11900, 4500, 2000)
    OP_0D()
    Sleep(800)

    OP_23(0x0067)

    def _loc_621(): pass

    label('loc_621')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AA',
    )

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_653'),
        (0x00000001, 'loc_65F'),
        (0x00000002, 'loc_66B'),
        (0x00000003, 'loc_677'),
        (0x00000004, 'loc_683'),
        (0x00000005, 'loc_68F'),
        (0x00000006, 'loc_69B'),
        (-1, 'loc_6A7'),
    )

    def _loc_653(): pass

    label('loc_653')

    NewScene('ED6_DT21/T3111._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_6A7')

    def _loc_65F(): pass

    label('loc_65F')

    NewScene('ED6_DT21/T3111._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_6A7')

    def _loc_66B(): pass

    label('loc_66B')

    NewScene('ED6_DT21/T3114._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_6A7')

    def _loc_677(): pass

    label('loc_677')

    NewScene('ED6_DT21/T3114._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_6A7')

    def _loc_683(): pass

    label('loc_683')

    NewScene('ED6_DT21/T3114._SN', 112, 0, 0)
    IdleLoop()

    Jump('loc_6A7')

    def _loc_68F(): pass

    label('loc_68F')

    NewScene('ED6_DT21/T3119._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_6A7')

    def _loc_69B(): pass

    label('loc_69B')

    NewScene('ED6_DT21/T3101._SN', 104, 0, 0)
    IdleLoop()

    Jump('loc_6A7')

    def _loc_6A7(): pass

    label('loc_6A7')

    Jump('loc_769')

    def _loc_6AA(): pass

    label('loc_6AA')

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6CF'),
        (0x00000001, 'loc_6E5'),
        (0x00000002, 'loc_6FB'),
        (0x00000003, 'loc_711'),
        (0x00000004, 'loc_727'),
        (0x00000005, 'loc_73D'),
        (0x00000006, 'loc_753'),
        (-1, 'loc_769'),
    )

    def _loc_6CF(): pass

    label('loc_6CF')

    PlaySE(14, 0x00, 0x64)
    Sleep(500)

    NewScene('ED6_DT21/T3111._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_769')

    def _loc_6E5(): pass

    label('loc_6E5')

    PlaySE(14, 0x00, 0x64)
    Sleep(500)

    NewScene('ED6_DT21/T3111._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_769')

    def _loc_6FB(): pass

    label('loc_6FB')

    PlaySE(14, 0x00, 0x64)
    Sleep(500)

    NewScene('ED6_DT21/T3114._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_769')

    def _loc_711(): pass

    label('loc_711')

    PlaySE(14, 0x00, 0x64)
    Sleep(500)

    NewScene('ED6_DT21/T3114._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_769')

    def _loc_727(): pass

    label('loc_727')

    PlaySE(14, 0x00, 0x64)
    Sleep(500)

    NewScene('ED6_DT21/T3114._SN', 112, 0, 0)
    IdleLoop()

    Jump('loc_769')

    def _loc_73D(): pass

    label('loc_73D')

    PlaySE(14, 0x00, 0x64)
    Sleep(500)

    NewScene('ED6_DT21/T3119._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_769')

    def _loc_753(): pass

    label('loc_753')

    PlaySE(14, 0x00, 0x64)
    Sleep(500)

    NewScene('ED6_DT21/T3101._SN', 104, 0, 0)
    IdleLoop()

    Jump('loc_769')

    def _loc_769(): pass

    label('loc_769')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
