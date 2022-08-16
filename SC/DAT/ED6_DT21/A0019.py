import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0019_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0019   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'A0006.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0x0003
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
        ScenaActorData(
            triggerX            = 1800,
            triggerZ            = 1000,
            triggerY            = 120,
            triggerRange        = 2000,
            actorX              = 1800,
            actorZ              = 1000,
            actorY              = 120,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4000,
            triggerZ            = 1000,
            triggerY            = 120,
            triggerRange        = 2000,
            actorX              = 4000,
            actorZ              = 1000,
            actorY              = 120,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF0
@scena.Code('Init')
def Init():
    AddItem(0x0383, 1)
    AddItem(ItemTable['夜视眼镜'], 1)

    Return()

# id: 0x0001 offset: 0xFB
@scena.Code('func_01_FB')
def func_01_FB():
    OP_BE(0x00, 0x01, 0x0002, 0x0028, 0x0000, 0x02, 1000, 0, 5000, 5000, 1000, 10000)
    OP_BE(0x01, 0x04, 0x0002, 0x0014, 0x0000, 0x01, 10000, -500, 2000, 6000, 1000, 0)
    OP_BE(0x02, 0x02, 0x0000, 0x003C, 0x0003, 0x00, 0, 0, 0, 0, 0, 0)
    OP_BF(0x02, 0x02, 2, 2000)
    OP_BF(0x02, 0x02, 3, 4000)
    OP_C1(0x80, 0x01, 0x0000003C)
    OP_C1(0x81, 0x01, 0x0000003C)
    OP_C1(0x82, 0x01, 0x0000003C)
    OP_C4(0x00, 0x00000001)

    Return()

# id: 0x0002 offset: 0x18B
@scena.Code('func_02_18B')
def func_02_18B():
    TalkBegin(0x00FF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B5',
    )

    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    Sleep(500)

    StopEffect(0x80, 0x02)
    StopEffect(0x81, 0x02)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_235')

    def _loc_1B5(): pass

    label('loc_1B5')

    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    Sleep(500)

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_235(): pass

    label('loc_235')

    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x239
@scena.Code('func_03_239')
def func_03_239():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x383),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE',
    )

    EventBegin(0x00)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    Sleep(500)

    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    Sleep(500)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    Sleep(500)

    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    Sleep(500)

    EventEnd(0x00)

    def _loc_2CE(): pass

    label('loc_2CE')

    Return()

# id: 0x0004 offset: 0x2CF
@scena.Code('func_04_2CF')
def func_04_2CF():
    TalkBegin(0x00FF)
    OP_18(0x00, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x383),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FA',
    )

    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)

    def _loc_2FA(): pass

    label('loc_2FA')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
