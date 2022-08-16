import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0402.x'
    header.mapIndex       = 16
    header.bgm            = 33
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
            word_3A         = 16,
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
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10150._CH', 'ED6_DT09/CH10150P._CP'),
        ('ED6_DT09/CH10151._CH', 'ED6_DT09/CH10151P._CP'),
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT09/CH10041._CH', 'ED6_DT09/CH10041P._CP'),
        ('ED6_DT09/CH10190._CH', 'ED6_DT09/CH10190P._CP'),
        ('ED6_DT09/CH10191._CH', 'ED6_DT09/CH10191P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '波波',
            x           = -51000,
            z           = 0,
            y           = 1000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '食人鲨',
            x           = -42000,
            z           = 0,
            y           = 11000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0039,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '波波',
            x           = -42000,
            z           = 0,
            y           = 27000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '食人鲨',
            x           = -52000,
            z           = 0,
            y           = 37000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0039,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '波波',
            x           = -68000,
            z           = 0,
            y           = 37000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '食人鲨',
            x           = -78000,
            z           = 0,
            y           = 27000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0039,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '波波',
            x           = -78000,
            z           = 0,
            y           = 11000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '竹刀飞鱼',
            x           = -48000,
            z           = 0,
            y           = 19000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '竹刀飞鱼',
            x           = -59000,
            z           = 0,
            y           = 7000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0037,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '竹刀飞鱼',
            x           = -72000,
            z           = 0,
            y           = 19000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0037,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '岩溶捕猎手',
            x           = -60000,
            z           = 0,
            y           = 19000,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x21E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -46000,
            y           = -1000,
            z           = 5000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -58000,
            y           = -1000,
            z           = 3400,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -44200,
            y           = -1000,
            z           = 17000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -44200,
            y           = -1000,
            z           = 21000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -46000,
            y           = -1000,
            z           = 33000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -60000,
            y           = -1000,
            z           = 39000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = -62000,
            y           = -1000,
            z           = 34800,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = -75800,
            y           = -1000,
            z           = 21000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = -80000,
            y           = -1000,
            z           = 19000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = -68600,
            y           = -1000,
            z           = 10300,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -51300,
            y           = -1000,
            z           = 10300,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = -68700,
            y           = -1000,
            z           = 27700,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = -51500,
            y           = -1000,
            z           = 27700,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000F,
        ),
        ScenaEventData(
            x           = -75800,
            y           = -1000,
            z           = 17000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = -66000,
            y           = -1000,
            z           = 19000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = -54000,
            y           = -1000,
            z           = 19000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -60000,
            y           = -1000,
            z           = 13000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = -60000,
            y           = -1000,
            z           = 25000,
            range       = 2000,
            dword_10    = 0x000001F4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000014,
        ),
    )

# id: 0x10004 offset: 0x45E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -54300,
            triggerZ            = 800,
            triggerY            = 33000,
            triggerRange        = 1000,
            actorX              = -54300,
            actorZ              = 800,
            actorY              = 33000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x482
@scena.Code('Init')
def Init():
    OP_72(0x0000, 0x0010)

    Return()

# id: 0x0001 offset: 0x488
@scena.Code('func_01_488')
def func_01_488():
    Return()

# id: 0x0002 offset: 0x489
@scena.Code('func_02_489')
def func_02_489():
    OP_75(0x01, 0x00000000, 0x00)
    OP_75(0x02, 0x00000000, 0x00)
    OP_75(0x03, 0x00000000, 0x00)
    OP_75(0x04, 0x00000000, 0x00)
    OP_75(0x05, 0x00000000, 0x00)
    OP_75(0x06, 0x00000000, 0x00)
    OP_75(0x07, 0x00000000, 0x00)
    OP_75(0x08, 0x00000000, 0x00)
    OP_75(0x09, 0x00000000, 0x00)
    OP_75(0x0A, 0x00000000, 0x00)
    OP_75(0x0B, 0x00000000, 0x00)
    OP_75(0x0C, 0x00000000, 0x00)
    OP_75(0x0D, 0x00000000, 0x00)
    OP_75(0x0E, 0x00000000, 0x00)
    OP_75(0x0F, 0x00000000, 0x00)
    OP_75(0x10, 0x00000000, 0x00)
    OP_75(0x11, 0x00000000, 0x00)
    OP_75(0x12, 0x00000000, 0x00)
    OP_75(0x13, 0x00000000, 0x00)
    OP_75(0x14, 0x00000000, 0x00)
    OP_75(0x15, 0x00000000, 0x00)
    OP_75(0x16, 0x00000000, 0x00)
    OP_75(0x17, 0x00000000, 0x00)
    OP_75(0x18, 0x00000000, 0x00)
    OP_75(0x19, 0x00000000, 0x00)
    OP_75(0x1A, 0x00000000, 0x00)
    OP_75(0x1B, 0x00000000, 0x00)
    OP_75(0x1C, 0x00000000, 0x00)
    OP_75(0x1D, 0x00000000, 0x00)
    OP_75(0x1E, 0x00000000, 0x00)
    OP_75(0x1F, 0x00000000, 0x00)
    OP_75(0x20, 0x00000000, 0x00)
    OP_75(0x21, 0x00000000, 0x00)
    OP_75(0x22, 0x00000000, 0x00)
    OP_75(0x23, 0x00000000, 0x00)
    OP_75(0x24, 0x00000000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ClearScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    ClearScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ClearScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    ClearScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ClearScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ClearScenaFlags(ScenaFlag(0x0002, 0, 0x10))
    ClearScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    Return()

# id: 0x0003 offset: 0x5B9
@scena.Code('func_03_5B9')
def func_03_5B9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F2',
    )

    OP_76(0x0001, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x0022, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5F2(): pass

    label('loc_5F2')

    Return()

# id: 0x0004 offset: 0x5F3
@scena.Code('func_04_5F3')
def func_04_5F3():
    OP_76(0x0002, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x0023, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x0005 offset: 0x622
@scena.Code('func_05_622')
def func_05_622():
    OP_76(0x0003, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x0021, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x0006 offset: 0x651
@scena.Code('func_06_651')
def func_06_651():
    OP_76(0x0004, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x0020, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x0007 offset: 0x680
@scena.Code('func_07_680')
def func_07_680():
    OP_76(0x0005, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x001F, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x0008 offset: 0x6AF
@scena.Code('func_08_6AF')
def func_08_6AF():
    OP_76(0x0006, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x001E, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x0009 offset: 0x6DE
@scena.Code('func_09_6DE')
def func_09_6DE():
    OP_76(0x0007, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x001D, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x000A offset: 0x70D
@scena.Code('func_0A_70D')
def func_0A_70D():
    OP_76(0x0008, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x001B, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x000B offset: 0x73C
@scena.Code('func_0B_73C')
def func_0B_73C():
    OP_76(0x0009, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x001C, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)
    Call(0, 0x0015)

    Return()

# id: 0x000C offset: 0x76F
@scena.Code('func_0C_76F')
def func_0C_76F():
    OP_76(0x000A, 0x00000000, 0x0002, 8, 8, 100, 0x08, 0x0F)
    OP_76(0x0024, 0x00000000, 0x0002, 4, 4, 100, 0x08, 0x0F)

    Return()

# id: 0x000D offset: 0x79E
@scena.Code('func_0D_79E')
def func_0D_79E():
    OP_76(0x000B, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x0019, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x000E offset: 0x7CD
@scena.Code('func_0E_7CD')
def func_0E_7CD():
    OP_76(0x000C, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x0017, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x000F offset: 0x7FC
@scena.Code('func_0F_7FC')
def func_0F_7FC():
    OP_76(0x000D, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x0018, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x0010 offset: 0x82B
@scena.Code('func_10_82B')
def func_10_82B():
    OP_76(0x000E, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x001A, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x0011 offset: 0x85A
@scena.Code('func_11_85A')
def func_11_85A():
    OP_76(0x000F, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x0016, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x0012 offset: 0x889
@scena.Code('func_12_889')
def func_12_889():
    OP_76(0x0010, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x0014, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x0013 offset: 0x8B8
@scena.Code('func_13_8B8')
def func_13_8B8():
    OP_76(0x0011, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x0013, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x0014 offset: 0x8E7
@scena.Code('func_14_8E7')
def func_14_8E7():
    OP_76(0x0012, 0x00000000, 0x0002, 8, 8, 100, 0x00, 0x07)
    OP_76(0x0015, 0x00000000, 0x0002, 4, 4, 100, 0x00, 0x07)

    Return()

# id: 0x0015 offset: 0x916
@scena.Code('func_15_916')
def func_15_916():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_91E',
    )

    Return()

    def _loc_91E(): pass

    label('loc_91E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_926',
    )

    Return()

    def _loc_926(): pass

    label('loc_926')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_92E',
    )

    Return()

    def _loc_92E(): pass

    label('loc_92E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_936',
    )

    Return()

    def _loc_936(): pass

    label('loc_936')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_93E',
    )

    Return()

    def _loc_93E(): pass

    label('loc_93E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_946',
    )

    Return()

    def _loc_946(): pass

    label('loc_946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_94E',
    )

    Return()

    def _loc_94E(): pass

    label('loc_94E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_956',
    )

    Return()

    def _loc_956(): pass

    label('loc_956')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
