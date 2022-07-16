import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4212_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4212   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '赫穆特'),
    TXT(0x02, '达扬'),
    TXT(0x03, '托克斯'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4212.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x704
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -70580,
            z                   = 0,
            y                   = -37370,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -61220,
            z                   = 0,
            y                   = -35100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -67090,
            z                   = 0,
            y                   = -31900,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x13A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x13A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x13A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_164',
    )

    SetChrChipByIndex(0x0000, 0)
    SetChrChipByIndex(0x0001, 1)
    SetChrChipByIndex(0x0138, 2)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)

    def _loc_164(): pass

    label('loc_164')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_178',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)

    Jump('loc_1A7')

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_182',
    )

    Jump('loc_1A7')

    def _loc_182(): pass

    label('loc_182')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_18C',
    )

    Jump('loc_1A7')

    def _loc_18C(): pass

    label('loc_18C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_196',
    )

    Jump('loc_1A7')

    def _loc_196(): pass

    label('loc_196')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_1A0',
    )

    Jump('loc_1A7')

    def _loc_1A0(): pass

    label('loc_1A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_1A7',
    )

    def _loc_1A7(): pass

    label('loc_1A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1B6',
    )

    ClearChrFlags(0x0008, 0x0080)

    Jump('loc_217')

    def _loc_1B6(): pass

    label('loc_1B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1C0',
    )

    Jump('loc_217')

    def _loc_1C0(): pass

    label('loc_1C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1CA',
    )

    Jump('loc_217')

    def _loc_1CA(): pass

    label('loc_1CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1D4',
    )

    Jump('loc_217')

    def _loc_1D4(): pass

    label('loc_1D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1DE',
    )

    Jump('loc_217')

    def _loc_1DE(): pass

    label('loc_1DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1E8',
    )

    Jump('loc_217')

    def _loc_1E8(): pass

    label('loc_1E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F2',
    )

    Jump('loc_217')

    def _loc_1F2(): pass

    label('loc_1F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1FC',
    )

    Jump('loc_217')

    def _loc_1FC(): pass

    label('loc_1FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_206',
    )

    Jump('loc_217')

    def _loc_206(): pass

    label('loc_206')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_210',
    )

    Jump('loc_217')

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_217',
    )

    def _loc_217(): pass

    label('loc_217')

    Return()

# id: 0x0001 offset: 0x218
@scena.Code('Init')
def Init():
    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x222
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_237',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_237(): pass

    label('loc_237')

    Return()

# id: 0x0003 offset: 0x238
@scena.Code('func_03_238')
def func_03_238():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_245',
    )

    Jump('loc_336')

    def _loc_245(): pass

    label('loc_245')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_290',
    )

    ChrTalk(
        0x00FE,
        (
            '外出休假的人员\n',
            '终于回到城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在开始可有的忙了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336')

    def _loc_290(): pass

    label('loc_290')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_29A',
    )

    Jump('loc_336')

    def _loc_29A(): pass

    label('loc_29A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_2A4',
    )

    Jump('loc_336')

    def _loc_2A4(): pass

    label('loc_2A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_2C8',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，今天又要加班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_336')

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_336',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，不管怎么说，\n',
            '现在的人手是不足以完成任务的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其他的人\n',
            '都被公爵以休假的名义\n',
            '给赶出城去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_336(): pass

    label('loc_336')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x33A
@scena.Code('func_04_33A')
def func_04_33A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_347',
    )

    Jump('loc_5A8')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3BD',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，政变残留问题的处理\n',
            '和一些手头的工作简直堆积如山。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天又只有加班了……\n',
            '在王城里做事太辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A8')

    def _loc_3BD(): pass

    label('loc_3BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_3C7',
    )

    Jump('loc_5A8')

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_3D1',
    )

    Jump('loc_5A8')

    def _loc_3D1(): pass

    label('loc_3D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_4A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_422',
    )

    ChrTalk(
        0x00FE,
        (
            '呜呜……\n',
            '只是想象一下公爵大权在握的样子，\n',
            '就感到一阵寒意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49D')

    def _loc_422(): pass

    label('loc_422')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '虽说公爵是女王陛下的代理人，\n',
            '但做出决定性指示的却是情报部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有理查德上校的话，\n',
            '还不知道会变成什么样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49D(): pass

    label('loc_49D')

    Jump('loc_5A8')

    def _loc_4A0(): pass

    label('loc_4A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_5A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_522',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是处理利贝尔王国\n',
            '政务的重要办公地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在女王陛下病了，\n',
            '但仍然接受杜南公爵的指示\n',
            '来执行公务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A8')

    def _loc_522(): pass

    label('loc_522')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这里是行政区域。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是处理利贝尔王国\n',
            '政务的重要办公地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在女王陛下病了，\n',
            '但仍然接受杜南公爵的指示\n',
            '来执行公务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A8(): pass

    label('loc_5A8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x5AC
@scena.Code('func_05_5AC')
def func_05_5AC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_693',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5ED',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，我最喜欢的钓鱼\n',
            '看来也暂时没空去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_690')

    def _loc_5ED(): pass

    label('loc_5ED')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '今天开始\n',
            '又要继续工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为公爵经常无所事事，\n',
            '我还以为可以一直休息了，\n',
            '没想到竟然发生了那么多事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来要收拾残局\n',
            '可是要花相当的功夫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_690(): pass

    label('loc_690')

    Jump('loc_6F4')

    def _loc_693(): pass

    label('loc_693')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_69D',
    )

    Jump('loc_6F4')

    def _loc_69D(): pass

    label('loc_69D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6A7',
    )

    Jump('loc_6F4')

    def _loc_6A7(): pass

    label('loc_6A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6B1',
    )

    Jump('loc_6F4')

    def _loc_6B1(): pass

    label('loc_6B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_6BB',
    )

    Jump('loc_6F4')

    def _loc_6BB(): pass

    label('loc_6BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_6C5',
    )

    Jump('loc_6F4')

    def _loc_6C5(): pass

    label('loc_6C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_6CF',
    )

    Jump('loc_6F4')

    def _loc_6CF(): pass

    label('loc_6CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_6D9',
    )

    Jump('loc_6F4')

    def _loc_6D9(): pass

    label('loc_6D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_6E3',
    )

    Jump('loc_6F4')

    def _loc_6E3(): pass

    label('loc_6E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_6ED',
    )

    Jump('loc_6F4')

    def _loc_6ED(): pass

    label('loc_6ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_6F4',
    )

    def _loc_6F4(): pass

    label('loc_6F4')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
