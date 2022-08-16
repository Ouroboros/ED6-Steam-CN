import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3114_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3114_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3114.x'
    header.mapIndex       = 1
    header.bgm            = 10
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C4',
    )

    Return()

    def _loc_C4(): pass

    label('loc_C4')

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x01, 0x0100)"),
            Expr.Ez,
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C5',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-107170, 0, -700, 0)
    ChrSetPos(0x0101, -107070, 0, -2860, 2)
    ChrSetPos(0x0102, -108010, 0, -2670, 359)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_134',
    )

    ChrSetPos(0x0107, -105720, 0, -2270, 332)

    def _loc_134(): pass

    label('loc_134')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_153',
    )

    ChrSetPos(0x0106, -109230, 0, -1920, 56)

    def _loc_153(): pass

    label('loc_153')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_172',
    )

    ChrSetPos(0x013C, -106920, 0, -560, 21)

    def _loc_172(): pass

    label('loc_172')

    OP_0D()
    Sleep(400)

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181098V喵呀～～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181099V#004F咦…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013C, 0x0101, 400)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181098V喵呀～～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181101V#014F……对这道门有反应吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181102V#064F这、这个房间是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181103V#002F不管怎样，\n',
            '先进去调查再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181104V#012F嗯，说得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x01, 0x0100)
    OP_B2(0x00, 0x03, 0x0080)
    EventEnd(0x00)

    def _loc_2C5(): pass

    label('loc_2C5')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
