import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0001_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0001_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map'
    header.mapModel       = 'T0001.x'
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
            preInitFunction = 0x0001,
            initScena       = 0x0000,
            initFunction    = 0x0002,
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
    Talk(
        (
            TxtCtl.ShowAll,
            '请选择魔兽',
            TxtCtl.Enter,
        ),
    )

    def _loc_B6(): pass

    label('loc_B6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C5',
    )

    Menu(
        1,
        10,
        100,
        1,
        (
            TXT(0x00, '测试\n'),
            TXT(0x01, '10000 嗜杀巨蟹\n'),
            TXT(0x02, '10260 红茶钳虫\n'),
            TXT(0x03, '10180 爆种铃兰\n'),
            TXT(0x04, '10010 巨型黄蜂（Giant Wasp）\n'),
            TXT(0x05, '10020 跳跳猫\n'),
            TXT(0x06, '10210 火爆麻雀\n'),
            TXT(0x07, '10190 岩溶捕猎手\n'),
            TXT(0x08, '11050 田鼠管理员\n'),
            TXT(0x09, '10280 森林之雾\n'),
            TXT(0x0A, '10230 菠萝怪\n'),
            TXT(0x0B, '10240 多角铁牛\n'),
            TXT(0x0C, '10050 剑齿吸血魔ＤＸ\n'),
            TXT(0x0D, '取消\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1DE'),
        (0x00000001, 'loc_1EE'),
        (0x00000002, 'loc_1FE'),
        (0x00000003, 'loc_20E'),
        (0x00000004, 'loc_21E'),
        (0x00000005, 'loc_22E'),
        (0x00000006, 'loc_23E'),
        (0x00000007, 'loc_24E'),
        (0x00000008, 'loc_25E'),
        (0x00000009, 'loc_26E'),
        (0x0000000A, 'loc_27E'),
        (0x0000000B, 'loc_28E'),
        (0x0000000C, 'loc_29E'),
        (-1, 'loc_2AE'),
    )

    def _loc_1DE(): pass

    label('loc_1DE')

    Battle(0x000007D1, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_1EE(): pass

    label('loc_1EE')

    Battle(0x000007DA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_1FE(): pass

    label('loc_1FE')

    Battle(0x000007DB, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_20E(): pass

    label('loc_20E')

    Battle(0x00000018, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_21E(): pass

    label('loc_21E')

    Battle(0x000007DD, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_22E(): pass

    label('loc_22E')

    Battle(0x0000007A, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_23E(): pass

    label('loc_23E')

    Battle(0x0000006E, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_24E(): pass

    label('loc_24E')

    Battle(0x0000003C, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_25E(): pass

    label('loc_25E')

    Battle(0x000007DF, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_26E(): pass

    label('loc_26E')

    Battle(0x00000042, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_27E(): pass

    label('loc_27E')

    Battle(0x00000045, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_28E(): pass

    label('loc_28E')

    Battle(0x00000048, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_29E(): pass

    label('loc_29E')

    Battle(0x000007D0, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_2B8')

    def _loc_2AE(): pass

    label('loc_2AE')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2B8(): pass

    label('loc_2B8')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B6')

    def _loc_2C5(): pass

    label('loc_2C5')

    OP_5F(0x0001)
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
